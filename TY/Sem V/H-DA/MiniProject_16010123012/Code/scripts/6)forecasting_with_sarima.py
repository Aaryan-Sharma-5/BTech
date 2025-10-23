"""
SARIMA Forecasting Script
Seasonal ARIMA model for humidity prediction with:
- Automated seasonal parameter selection
- Seasonal decomposition analysis
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
import warnings
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
import itertools
import logging

warnings.filterwarnings("ignore")

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configuration
CONFIG = {
    'input_file': 'data/cleaned_humidity.csv',
    'output_file': 'data/forecast_results_sarima.csv',
    'train_ratio': 0.8,
    'seasonal_period': 12,  # Monthly seasonality
    'p_range': range(0, 2),
    'd_range': range(0, 2),
    'q_range': range(0, 2),
    'P_range': range(0, 2),
    'D_range': range(0, 2),
    'Q_range': range(0, 2)
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

def visualize_seasonality(df):
    """Visualize potential seasonality in the data"""
    plt.figure(figsize=(14, 6))
    plt.plot(df.index, df['humidity'], linewidth=0.8, alpha=0.7, color='blue')
    
    # Add rolling average to highlight trend
    rolling_mean = df['humidity'].rolling(window=30).mean()
    plt.plot(df.index, rolling_mean, linewidth=2, color='red', 
             label='30-day Moving Average', alpha=0.8)
    
    plt.title("Humidity Over Time — Checking for Seasonality", 
              fontsize=14, fontweight='bold')
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Humidity (%)", fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('outputs/visualizations/sarima_seasonality_check.png', dpi=300, bbox_inches='tight')
    logger.info("Saved: sarima_seasonality_check.png")
    plt.show()

def grid_search_sarima(train_data, p_range, d_range, q_range, 
                       P_range, D_range, Q_range, seasonal_period):
    """
    Perform grid search for optimal SARIMA parameters
    
    Args:
        train_data: Training time series
        p_range, d_range, q_range: Non-seasonal parameter ranges
        P_range, D_range, Q_range: Seasonal parameter ranges
        seasonal_period: Seasonal period (m)
    
    Returns:
        tuple: (best_params, best_seasonal_params, best_aic, results)
    """
    logger.info("Starting SARIMA parameter grid search...")
    
    # Generate all combinations
    pdq = list(itertools.product(p_range, d_range, q_range))
    seasonal_pdq = [(x[0], x[1], x[2], seasonal_period) 
                    for x in itertools.product(P_range, D_range, Q_range)]
    
    total_combinations = len(pdq) * len(seasonal_pdq)
    logger.info(f"Testing {total_combinations} parameter combinations...")
    logger.info(f"Seasonal period (m): {seasonal_period} months")
    
    best_aic = float("inf")
    best_params = None
    results = []
    
    tested = 0
    for param in pdq:
        for param_seasonal in seasonal_pdq:
            tested += 1
            try:
                model = SARIMAX(train_data,
                               order=param,
                               seasonal_order=param_seasonal,
                               enforce_stationarity=False,
                               enforce_invertibility=False)
                results_fit = model.fit(disp=False, maxiter=200)
                aic = results_fit.aic
                
                results.append({
                    'order': param,
                    'seasonal_order': param_seasonal,
                    'AIC': aic,
                    'BIC': results_fit.bic
                })
                
                if aic < best_aic:
                    best_aic = aic
                    best_params = (param, param_seasonal)
                    logger.info(f"[{tested}/{total_combinations}] New best: "
                              f"SARIMA{param}x{param_seasonal} - AIC={aic:.2f}")
                    
            except Exception as e:
                continue
    
    logger.info(f"\n{'='*70}")
    logger.info(f"Grid Search Complete!")
    logger.info(f"Best SARIMA parameters: {best_params[0]} x {best_params[1]}")
    logger.info(f"Best AIC: {best_aic:.2f}")
    logger.info(f"{'='*70}\n")
    
    return best_params, best_aic, results

def analyze_residuals(residuals, title="SARIMA Residual Analysis"):
    """Perform comprehensive residual analysis"""
    logger.info(f"\n{title}")
    logger.info("="*70)
    
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
    axes[1, 0].set_title('ACF of Residuals', fontweight='bold')
    axes[1, 0].grid(True, alpha=0.3)
    
    # 4. Q-Q plot
    from scipy import stats
from pathlib import Path

# Ensure required directories exist
Path('data').mkdir(parents=True, exist_ok=True)
Path('outputs/visualizations').mkdir(parents=True, exist_ok=True)
Path('outputs/metrics').mkdir(parents=True, exist_ok=True)
    stats.probplot(residuals.dropna(), dist="norm", plot=axes[1, 1])
    axes[1, 1].set_title('Q-Q Plot', fontweight='bold')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('outputs/visualizations/sarima_residual_analysis.png', dpi=300, bbox_inches='tight')
    logger.info("Saved: sarima_residual_analysis.png")
    plt.show()
    
    # Ljung-Box test
    lb_test = acorr_ljungbox(residuals.dropna(), lags=[10], return_df=True)
    print(f"\nLjung-Box Test:")
    print(lb_test)
    
    if lb_test['lb_pvalue'].values[0] > 0.05:
        print("[SUCCESS] Residuals are white noise (p > 0.05)")
    else:
        print("[WARNING] Residuals may have autocorrelation (p <= 0.05)")
    
    logger.info("="*70)

def plot_forecast_with_confidence(train, test, forecast_result, best_params):
    """Plot forecast with confidence intervals"""
    forecast_df = forecast_result.summary_frame()
    
    plt.figure(figsize=(14, 7))
    
    # Plot training data
    plt.plot(train.index, train['humidity'], label='Training Data', 
             color='blue', linewidth=1, alpha=0.7)
    
    # Plot test data
    plt.plot(test.index, test['humidity'], label='Actual Test Data', 
             color='green', linewidth=1.5, alpha=0.8)
    
    # Plot forecast
    plt.plot(forecast_df.index, forecast_df['mean'], label='SARIMA Forecast', 
             color='red', linewidth=2)
    
    # Plot confidence intervals
    plt.fill_between(forecast_df.index, 
                     forecast_df['mean_ci_lower'], 
                     forecast_df['mean_ci_upper'], 
                     color='red', alpha=0.2, label='95% Confidence Interval')
    
    plt.title(f"SARIMA{best_params[0]}x{best_params[1]} Humidity Forecast", 
              fontsize=14, fontweight='bold')
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Humidity (%)", fontsize=12)
    plt.legend(loc='best')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('sarima_forecast_with_ci.png', dpi=300, bbox_inches='tight')
    logger.info("Saved: sarima_forecast_with_ci.png")
    plt.show()

def main():
    """Main SARIMA forecasting pipeline"""
    logger.info("Starting SARIMA Forecasting Pipeline...")
    
    # Load data
    df = load_and_prepare_data(CONFIG['input_file'])
    if df is None:
        return
    
    # Visualize seasonality
    logger.info("\nVisualizing potential seasonality...")
    visualize_seasonality(df)
    
    # Train-test split
    train_size = int(len(df) * CONFIG['train_ratio'])
    train, test = df[:train_size], df[train_size:]
    
    logger.info(f"\nTrain size: {len(train)} records")
    logger.info(f"Test size: {len(test)} records")
    
    # Grid search for best parameters
    best_params, best_aic, all_results = grid_search_sarima(
        train['humidity'],
        CONFIG['p_range'], CONFIG['d_range'], CONFIG['q_range'],
        CONFIG['P_range'], CONFIG['D_range'], CONFIG['Q_range'],
        CONFIG['seasonal_period']
    )
    
    # Fit final model
    logger.info(f"\nFitting final SARIMA model...")
    model = SARIMAX(train['humidity'],
                    order=best_params[0],
                    seasonal_order=best_params[1],
                    enforce_stationarity=False,
                    enforce_invertibility=False)
    model_fit = model.fit(disp=False, maxiter=200)
    
    # Print model summary
    print("\n" + "="*70)
    print("SARIMA Model Summary")
    print("="*70)
    print(model_fit.summary())
    
    # Analyze residuals
    residuals = model_fit.resid
    analyze_residuals(residuals)
    
    # Forecast
    logger.info(f"\nGenerating forecast for {len(test)} periods...")
    forecast_result = model_fit.get_forecast(steps=len(test))
    forecast = forecast_result.predicted_mean
    
    # Plot forecast with confidence intervals
    plot_forecast_with_confidence(train, test, forecast_result, best_params)
    
    # Save results
    forecast_df = pd.DataFrame({
        "date": test.index,
        "forecast": forecast.values,
        "lower_ci": forecast_result.summary_frame()['mean_ci_lower'].values,
        "upper_ci": forecast_result.summary_frame()['mean_ci_upper'].values
    })
    forecast_df.to_csv(CONFIG['output_file'], index=False)
    logger.info(f"[SUCCESS] SARIMA forecast saved to {CONFIG['output_file']}")
    
    # Save parameter search results
    results_df = pd.DataFrame(all_results).sort_values('AIC').head(10)
    results_df.to_csv('outputs/metrics/sarima_parameter_search_results.csv', index=False)
    logger.info("[SUCCESS] Parameter search results saved to sarima_parameter_search_results.csv")
    
    print("\n" + "="*70)
    print("Top 5 SARIMA Parameter Combinations:")
    print("="*70)
    print(results_df.head())

if __name__ == "__main__":
    main()
