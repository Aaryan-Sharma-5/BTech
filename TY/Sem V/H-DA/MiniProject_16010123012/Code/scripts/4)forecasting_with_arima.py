"""
ARIMA Forecasting Script
Builds ARIMA model for humidity prediction with:
- Automated parameter selection via grid search
- Model diagnostics and residual analysis
- Forecast visualization with confidence intervals
"""

import sys
import io
# Configure UTF-8 encoding for Windows console
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
import warnings
import logging

warnings.filterwarnings("ignore")

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configuration
CONFIG = {
    'input_file': 'data/cleaned_humidity.csv',
    'output_file': 'data/forecast_results.csv',
    'train_ratio': 0.8,
    'p_range': range(0, 4),
    'd_range': range(0, 2),
    'q_range': range(0, 4)
}

def load_and_prepare_data(filename):
    """Load and prepare data for modeling"""
    try:
        df = pd.read_csv(filename)
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)
        logger.info(f"[SUCCESS] Data loaded: {len(df)} records")
        logger.info(f"Date range: {df.index.min()} to {df.index.max()}")
        return df
    except FileNotFoundError:
        logger.error(f"File not found: {filename}")
        logger.error("Please run 2)data_processing.py first")
        return None

def grid_search_arima(train_data, p_values, d_values, q_values):
    """
    Perform grid search to find optimal ARIMA parameters
    
    Args:
        train_data: Training time series
        p_values: Range of AR orders to test
        d_values: Range of differencing orders to test
        q_values: Range of MA orders to test
    
    Returns:
        tuple: (best_order, best_aic, results_dict)
    """
    logger.info("Starting ARIMA parameter grid search...")
    
    best_aic = float("inf")
    best_order = None
    results = []
    
    total_combinations = len(p_values) * len(d_values) * len(q_values)
    logger.info(f"Testing {total_combinations} parameter combinations...")
    
    for p in p_values:
        for d in d_values:
            for q in q_values:
                try:
                    model = ARIMA(train_data, order=(p, d, q))
                    model_fit = model.fit()
                    aic = model_fit.aic
                    
                    results.append({
                        'order': (p, d, q),
                        'AIC': aic,
                        'BIC': model_fit.bic
                    })
                    
                    if aic < best_aic:
                        best_aic = aic
                        best_order = (p, d, q)
                        logger.info(f"New best: ARIMA{best_order} with AIC={best_aic:.2f}")
                        
                except Exception as e:
                    continue
    
    logger.info(f"\n{'='*60}")
    logger.info(f"Grid Search Complete!")
    logger.info(f"Best ARIMA parameters: {best_order}")
    logger.info(f"Best AIC: {best_aic:.2f}")
    logger.info(f"{'='*60}\n")
    
    return best_order, best_aic, results

def analyze_residuals(residuals, title="Residual Analysis"):
    """
    Perform comprehensive residual analysis
    
    Args:
        residuals: Model residuals
        title: Title for the analysis
    """
    logger.info(f"\n{title}")
    logger.info("="*60)
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # 1. Residuals over time
    axes[0, 0].plot(residuals, linewidth=0.8, color='blue')
    axes[0, 0].axhline(y=0, color='red', linestyle='--', linewidth=1)
    axes[0, 0].set_title('Residuals Over Time', fontweight='bold')
    axes[0, 0].set_xlabel('Date')
    axes[0, 0].set_ylabel('Residual')
    axes[0, 0].grid(True, alpha=0.3)
    
    # 2. Residual distribution
    axes[0, 1].hist(residuals, bins=30, edgecolor='black', color='skyblue', alpha=0.7)
    axes[0, 1].axvline(residuals.mean(), color='red', linestyle='--', 
                       label=f'Mean: {residuals.mean():.4f}')
    axes[0, 1].set_title('Residual Distribution', fontweight='bold')
    axes[0, 1].set_xlabel('Residual Value')
    axes[0, 1].set_ylabel('Frequency')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    
    # 3. ACF of residuals
    plot_acf(residuals.dropna(), lags=40, ax=axes[1, 0], alpha=0.05)
    axes[1, 0].set_title('ACF of Residuals (Should be within blue area)', fontweight='bold')
    axes[1, 0].grid(True, alpha=0.3)
    
    # 4. Q-Q plot
    from scipy import stats
    stats.probplot(residuals.dropna(), dist="norm", plot=axes[1, 1])
    axes[1, 1].set_title('Q-Q Plot (Should be on red line)', fontweight='bold')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('outputs/visualizations/arima_residual_analysis.png', dpi=300, bbox_inches='tight')
    logger.info("Saved: arima_residual_analysis.png")
    plt.show()
    
    # Ljung-Box test for autocorrelation
    lb_test = acorr_ljungbox(residuals.dropna(), lags=[10], return_df=True)
    print(f"\nLjung-Box Test (tests if residuals are white noise):")
    print(lb_test)
    
    if lb_test['lb_pvalue'].values[0] > 0.05:
        print("[SUCCESS] Residuals appear to be white noise (p > 0.05)")
        print("   Status: Model has captured the patterns well")
    else:
        print("[WARNING] Residuals may have remaining autocorrelation (p <= 0.05)")
        print("   Status: Model might be improved with different parameters")
    
    # Normality test
    from scipy.stats import shapiro
from pathlib import Path

# Ensure required directories exist
Path('data').mkdir(parents=True, exist_ok=True)
Path('outputs/visualizations').mkdir(parents=True, exist_ok=True)
Path('outputs/metrics').mkdir(parents=True, exist_ok=True)
    stat, p_value = shapiro(residuals.dropna()[:5000])  # Limit for performance
    print(f"\nShapiro-Wilk Normality Test:")
    print(f"Statistic: {stat:.6f}, p-value: {p_value:.6f}")
    
    if p_value > 0.05:
        print("[SUCCESS] Residuals appear normally distributed (p > 0.05)")
    else:
        print("[WARNING] Residuals may not be perfectly normal (p <= 0.05)")
    
    logger.info("="*60)

def plot_forecast_with_confidence(train, test, forecast_result, best_order):
    """
    Plot forecast with confidence intervals
    
    Args:
        train: Training data
        test: Test data
        forecast_result: Forecast result object with confidence intervals
        best_order: Best ARIMA order
    """
    forecast_df = forecast_result.summary_frame()
    
    plt.figure(figsize=(14, 7))
    
    # Plot training data
    plt.plot(train.index, train['humidity'], label='Training Data', 
             color='blue', linewidth=1, alpha=0.7)
    
    # Plot test data
    plt.plot(test.index, test['humidity'], label='Actual Test Data', 
             color='green', linewidth=1.5, alpha=0.8)
    
    # Plot forecast
    plt.plot(forecast_df.index, forecast_df['mean'], label='ARIMA Forecast', 
             color='red', linewidth=2)
    
    # Plot confidence intervals
    plt.fill_between(forecast_df.index, 
                     forecast_df['mean_ci_lower'], 
                     forecast_df['mean_ci_upper'], 
                     color='red', alpha=0.2, label='95% Confidence Interval')
    
    plt.title(f"ARIMA{best_order} Humidity Forecast with Confidence Intervals", 
              fontsize=14, fontweight='bold')
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Humidity (%)", fontsize=12)
    plt.legend(loc='best')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('arima_forecast_with_ci.png', dpi=300, bbox_inches='tight')
    logger.info("Saved: arima_forecast_with_ci.png")
    plt.show()

def main():
    """Main ARIMA forecasting pipeline"""
    logger.info("Starting ARIMA Forecasting Pipeline...")
    
    # Load data
    df = load_and_prepare_data(CONFIG['input_file'])
    if df is None:
        return
    
    # Train-test split
    train_size = int(len(df) * CONFIG['train_ratio'])
    train, test = df[:train_size], df[train_size:]
    
    logger.info(f"\nTrain size: {len(train)} records ({df.index[0]} to {df.index[train_size-1]})")
    logger.info(f"Test size: {len(test)} records ({df.index[train_size]} to {df.index[-1]})")
    
    # Grid search for best parameters
    best_order, best_aic, all_results = grid_search_arima(
        train['humidity'],
        CONFIG['p_range'],
        CONFIG['d_range'],
        CONFIG['q_range']
    )
    
    # Fit final model with best parameters
    logger.info(f"\nFitting final ARIMA{best_order} model...")
    model = ARIMA(train['humidity'], order=best_order)
    model_fit = model.fit()
    
    # Print model summary
    print("\n" + "="*60)
    print("ARIMA Model Summary")
    print("="*60)
    print(model_fit.summary())
    
    # Analyze residuals
    residuals = model_fit.resid
    analyze_residuals(residuals, "ARIMA Model Residual Analysis")
    
    # Forecast with confidence intervals
    logger.info(f"\nGenerating forecast for {len(test)} periods...")
    forecast_result = model_fit.get_forecast(steps=len(test))
    forecast = forecast_result.predicted_mean
    
    # Plot forecast with confidence intervals
    plot_forecast_with_confidence(train, test, forecast_result, best_order)
    
    # Save forecast results
    forecast_df = pd.DataFrame({
        "date": test.index,
        "forecast": forecast.values,
        "lower_ci": forecast_result.summary_frame()['mean_ci_lower'].values,
        "upper_ci": forecast_result.summary_frame()['mean_ci_upper'].values
    })
    forecast_df.to_csv(CONFIG['output_file'], index=False)
    logger.info(f"[SUCCESS] Forecast saved to {CONFIG['output_file']}")
    
    # Save top 10 parameter combinations
    results_df = pd.DataFrame(all_results).sort_values('AIC').head(10)
    results_df.to_csv('outputs/metrics/arima_parameter_search_results.csv', index=False)
    logger.info("[SUCCESS] Parameter search results saved to arima_parameter_search_results.csv")
    
    print("\n" + "="*60)
    print("Top 5 ARIMA Parameter Combinations:")
    print("="*60)
    print(results_df.head())

if __name__ == "__main__":
    main()
