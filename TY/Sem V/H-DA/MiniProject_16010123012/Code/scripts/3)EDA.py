"""
Exploratory Data Analysis (EDA) Script
Performs comprehensive analysis of humidity data including:
- Trend analysis
- Seasonality detection
- Stationarity tests (ADF test)
- ACF/PACF plots for ARIMA parameter selection
"""

import sys
import io
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
import logging
from pathlib import Path

# Ensure required directories exist
Path('data').mkdir(parents=True, exist_ok=True)
Path('outputs/visualizations').mkdir(parents=True, exist_ok=True)
Path('outputs/metrics').mkdir(parents=True, exist_ok=True)

# Set UTF-8 encoding for console output on Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

def load_data(filename='data/cleaned_humidity.csv'):
    """Load cleaned humidity data"""
    try:
        df = pd.read_csv(filename)
        df['date'] = pd.to_datetime(df['date'])
        logger.info(f"Data loaded successfully: {len(df)} records")
        return df
    except FileNotFoundError:
        logger.error(f"File not found: {filename}")
        logger.error("Please run 2)data_processing.py first")
        return None

def test_stationarity(timeseries, title='Time Series'):
    """
    Perform Augmented Dickey-Fuller test for stationarity
    
    Args:
        timeseries: Time series data
        title: Title for the test
    """
    logger.info(f"\n{'='*60}")
    logger.info(f"Augmented Dickey-Fuller Test - {title}")
    logger.info(f"{'='*60}")
    
    result = adfuller(timeseries.dropna())
    
    print(f'\nADF Statistic: {result[0]:.6f}')
    print(f'p-value: {result[1]:.6f}')
    print(f'Critical Values:')
    for key, value in result[4].items():
        print(f'\t{key}: {value:.3f}')
    
    if result[1] <= 0.05:
        print(f"\nResult: Data is STATIONARY (p-value = {result[1]:.6f} <= 0.05)")
        print("   Status: PASS - Can proceed with ARIMA modeling")
    else:
        print(f"\nResult: Data is NON-STATIONARY (p-value = {result[1]:.6f} > 0.05)")
        print("   Status: WARNING - Differencing may be needed (d > 0 in ARIMA)")
    
    logger.info(f"{'='*60}\n")

def plot_humidity_trend(df):
    """Plot daily humidity trend over time"""
    plt.figure(figsize=(14, 6))
    plt.plot(df['date'], df['humidity'], color='blue', linewidth=0.8, alpha=0.7)
    plt.title("Daily Humidity Trend — Ghatkopar (2023–2025)", fontsize=14, fontweight='bold')
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Humidity (%)", fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Add rolling average
    rolling_mean = df.set_index('date')['humidity'].rolling(window=30).mean()
    plt.plot(rolling_mean.index, rolling_mean.values, color='red', linewidth=2, 
             label='30-day Moving Average', alpha=0.8)
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('outputs/visualizations/humidity_trend.png', dpi=300, bbox_inches='tight')
    logger.info("Saved: humidity_trend.png")
    plt.show()

def plot_monthly_analysis(df):
    """Plot monthly average humidity"""
    df['month'] = pd.to_datetime(df['date']).dt.month
    df['month_name'] = pd.to_datetime(df['date']).dt.month_name()
    monthly_avg = df.groupby('month')['humidity'].mean()
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=monthly_avg.index, y=monthly_avg.values, palette="Blues_d", hue=monthly_avg.index, legend=False)
    plt.title("Average Monthly Humidity", fontsize=14, fontweight='bold')
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Average Humidity (%)", fontsize=12)
    plt.xticks(range(12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    
    # Add value labels on bars
    for i, v in enumerate(monthly_avg.values):
        plt.text(i, v + 0.5, f'{v:.1f}%', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('outputs/visualizations/monthly_humidity.png', dpi=300, bbox_inches='tight')
    logger.info("Saved: monthly_humidity.png")
    plt.show()

def plot_seasonal_decomposition(df):
    """Decompose time series into trend, seasonal, and residual components"""
    logger.info("Performing seasonal decomposition...")
    
    df_indexed = df.set_index('date')
    
    # Perform decomposition (multiplicative model for humidity)
    decomposition = seasonal_decompose(df_indexed['humidity'], 
                                       model='additive', 
                                       period=365)  # Annual seasonality
    
    fig, axes = plt.subplots(4, 1, figsize=(14, 10))
    
    # Original
    axes[0].plot(df_indexed.index, df_indexed['humidity'], color='blue', linewidth=0.8)
    axes[0].set_ylabel('Original', fontsize=11)
    axes[0].set_title('Seasonal Decomposition of Humidity Time Series', 
                      fontsize=14, fontweight='bold')
    axes[0].grid(True, alpha=0.3)
    
    # Trend
    axes[1].plot(decomposition.trend, color='orange', linewidth=1.5)
    axes[1].set_ylabel('Trend', fontsize=11)
    axes[1].grid(True, alpha=0.3)
    
    # Seasonal
    axes[2].plot(decomposition.seasonal, color='green', linewidth=1)
    axes[2].set_ylabel('Seasonal', fontsize=11)
    axes[2].grid(True, alpha=0.3)
    
    # Residual
    axes[3].plot(decomposition.resid, color='red', linewidth=0.5)
    axes[3].set_ylabel('Residual', fontsize=11)
    axes[3].set_xlabel('Date', fontsize=11)
    axes[3].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('outputs/visualizations/seasonal_decomposition.png', dpi=300, bbox_inches='tight')
    logger.info("Saved: seasonal_decomposition.png")
    plt.show()

def plot_acf_pacf(df):
    """Plot ACF and PACF for determining ARIMA parameters"""
    logger.info("Generating ACF and PACF plots...")
    
    fig, axes = plt.subplots(2, 1, figsize=(14, 8))
    
    # ACF Plot
    plot_acf(df['humidity'], lags=40, ax=axes[0], alpha=0.05)
    axes[0].set_title('Autocorrelation Function (ACF) - Determines MA order (q)', 
                      fontsize=12, fontweight='bold')
    axes[0].set_xlabel('Lag', fontsize=11)
    axes[0].set_ylabel('ACF', fontsize=11)
    axes[0].grid(True, alpha=0.3)
    
    # PACF Plot
    plot_pacf(df['humidity'], lags=40, ax=axes[1], alpha=0.05)
    axes[1].set_title('Partial Autocorrelation Function (PACF) - Determines AR order (p)', 
                      fontsize=12, fontweight='bold')
    axes[1].set_xlabel('Lag', fontsize=11)
    axes[1].set_ylabel('PACF', fontsize=11)
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('outputs/visualizations/acf_pacf_plots.png', dpi=300, bbox_inches='tight')
    logger.info("Saved: acf_pacf_plots.png")
    plt.show()
    
    print("\nHow to interpret ACF/PACF plots:")
    print("   - ACF: Significant lags suggest MA(q) order")
    print("   - PACF: Significant lags suggest AR(p) order")
    print("   - Blue shaded area: 95% confidence interval")

def plot_yearly_comparison(df):
    """Compare humidity patterns across different years"""
    df['year'] = pd.to_datetime(df['date']).dt.year
    df['day_of_year'] = pd.to_datetime(df['date']).dt.dayofyear
    
    plt.figure(figsize=(14, 6))
    for year in df['year'].unique():
        year_data = df[df['year'] == year]
        plt.plot(year_data['day_of_year'], year_data['humidity'], 
                label=f'{year}', linewidth=1.5, alpha=0.7)
    
    plt.title('Yearly Humidity Comparison', fontsize=14, fontweight='bold')
    plt.xlabel('Day of Year', fontsize=12)
    plt.ylabel('Humidity (%)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('outputs/visualizations/yearly_comparison.png', dpi=300, bbox_inches='tight')
    logger.info("Saved: yearly_comparison.png")
    plt.show()

def main():
    """Main EDA pipeline"""
    logger.info("Starting Exploratory Data Analysis...")
    
    # Load data
    df = load_data()
    if df is None:
        return
    
    # 1. Humidity trend over time
    logger.info("\n1. Plotting humidity trend...")
    plot_humidity_trend(df)
    
    # 2. Monthly analysis
    logger.info("\n2. Analyzing monthly patterns...")
    plot_monthly_analysis(df)
    
    # 3. Stationarity test
    logger.info("\n3. Testing stationarity...")
    test_stationarity(df['humidity'], 'Original Humidity Data')
    
    # 4. ACF/PACF plots
    logger.info("\n4. Generating ACF/PACF plots for ARIMA parameters...")
    plot_acf_pacf(df)
    
    # 5. Seasonal decomposition
    logger.info("\n5. Performing seasonal decomposition...")
    plot_seasonal_decomposition(df)
    
    # 6. Yearly comparison
    logger.info("\n6. Comparing yearly patterns...")
    plot_yearly_comparison(df)
    
    logger.info("\n[SUCCESS] EDA completed successfully!")
    logger.info("Generated visualizations:")
    logger.info("  - humidity_trend.png")
    logger.info("  - monthly_humidity.png")
    logger.info("  - acf_pacf_plots.png")
    logger.info("  - seasonal_decomposition.png")
    logger.info("  - yearly_comparison.png")

if __name__ == "__main__":
    main()
