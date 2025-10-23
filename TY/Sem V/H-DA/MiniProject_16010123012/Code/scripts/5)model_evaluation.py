"""
ARIMA Model Evaluation Script
Comprehensive evaluation of ARIMA model performance with:
- Multiple error metrics (MAE, RMSE, MAPE, R²)
- Residual analysis
- Visualization of predictions vs actuals
"""

import sys
import io
# Configure UTF-8 encoding for Windows console
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, mean_absolute_percentage_error
import logging
from pathlib import Path

# Ensure required directories exist
Path('data').mkdir(parents=True, exist_ok=True)
Path('outputs/visualizations').mkdir(parents=True, exist_ok=True)
Path('outputs/metrics').mkdir(parents=True, exist_ok=True)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_data():
    """Load test data and forecast results"""
    try:
        # Load original data
        df = pd.read_csv("data/cleaned_humidity.csv")
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)
        
        # Get test split
        train_size = int(len(df) * 0.8)
        test = df[train_size:]
        
        # Load ARIMA forecast
        forecast_df = pd.read_csv("data/forecast_results.csv")
        forecast_df['date'] = pd.to_datetime(forecast_df['date'])
        forecast_df.set_index('date', inplace=True)
        
        logger.info("[SUCCESS] Data loaded successfully")
        return test, forecast_df
        
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        logger.error("Please run 4)forecasting_with_arima.py first")
        return None, None

def calculate_metrics(actual, predicted):
    """
    Calculate comprehensive error metrics
    
    Args:
        actual: Actual values
        predicted: Predicted values
    
    Returns:
        dict: Dictionary of metrics
    """
    mae = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    mape = mean_absolute_percentage_error(actual, predicted) * 100
    r2 = r2_score(actual, predicted)
    
    # Additional metrics
    mse = mean_squared_error(actual, predicted)
    mean_actual = np.mean(actual)
    mean_predicted = np.mean(predicted)
    
    # Normalized metrics
    nrmse = rmse / (actual.max() - actual.min()) * 100  # Normalized RMSE
    
    metrics = {
        'MAE': mae,
        'MSE': mse,
        'RMSE': rmse,
        'NRMSE (%)': nrmse,
        'MAPE (%)': mape,
        'R² Score': r2,
        'Mean Actual': mean_actual,
        'Mean Predicted': mean_predicted
    }
    
    return metrics

def print_metrics_report(metrics):
    """Print formatted metrics report"""
    print("\n" + "="*70)
    print("[EVALUATION] ARIMA MODEL EVALUATION METRICS")
    print("="*70)
    
    print(f"\n{'Metric':<25} {'Value':<20} {'Interpretation'}")
    print("-"*70)
    
    print(f"{'MAE (Mean Abs Error)':<25} {metrics['MAE']:<20.4f} Lower is better")
    print(f"{'MSE (Mean Sq Error)':<25} {metrics['MSE']:<20.4f} Lower is better")
    print(f"{'RMSE (Root MSE)':<25} {metrics['RMSE']:<20.4f} Lower is better")
    print(f"{'NRMSE (%)':<25} {metrics['NRMSE (%)']:<20.2f} Lower is better")
    print(f"{'MAPE (%)':<25} {metrics['MAPE (%)']:<20.2f} Lower is better")
    print(f"{'R² Score':<25} {metrics['R² Score']:<20.4f} Closer to 1 is better")
    
    print("\n" + "-"*70)
    print(f"{'Mean Actual Humidity':<25} {metrics['Mean Actual']:<20.2f}%")
    print(f"{'Mean Predicted Humidity':<25} {metrics['Mean Predicted']:<20.2f}%")
    print(f"{'Prediction Bias':<25} {metrics['Mean Predicted'] - metrics['Mean Actual']:<20.2f}%")
    print("="*70)
    
    # Performance interpretation
    print("\n[ANALYSIS] Performance Interpretation:")
    if metrics['MAPE (%)'] < 5:
        print("   [EXCELLENT] MAPE < 5% - Very accurate predictions")
    elif metrics['MAPE (%)'] < 10:
        print("   [GOOD] MAPE < 10% - Acceptable accuracy")
    elif metrics['MAPE (%)'] < 20:
        print("   [FAIR] MAPE < 20% - Moderate accuracy")
    else:
        print("   [POOR] MAPE >= 20% - Consider model improvement")
    
    if metrics['R² Score'] > 0.8:
        print("   [STRONG] Strong correlation: R² > 0.8 - Model explains variance well")
    elif metrics['R² Score'] > 0.6:
        print("   [MODERATE] Moderate correlation: R² > 0.6 - Reasonable fit")
    else:
        print("   [WEAK] Weak correlation: R² <= 0.6 - Model may need improvement")

def plot_predictions_vs_actual(test, forecast_df):
    """Plot actual vs predicted values"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    
    # 1. Time series comparison
    axes[0, 0].plot(test.index, test['humidity'], label='Actual', 
                    color='green', linewidth=2, marker='o', markersize=3, alpha=0.7)
    axes[0, 0].plot(forecast_df.index, forecast_df['forecast'], label='Predicted', 
                    color='red', linewidth=2, marker='s', markersize=3, alpha=0.7)
    
    # Add confidence intervals if available
    if 'lower_ci' in forecast_df.columns and 'upper_ci' in forecast_df.columns:
        axes[0, 0].fill_between(forecast_df.index, 
                                forecast_df['lower_ci'], 
                                forecast_df['upper_ci'], 
                                color='red', alpha=0.2, label='95% CI')
    
    axes[0, 0].set_title('ARIMA: Actual vs Predicted Humidity', fontsize=12, fontweight='bold')
    axes[0, 0].set_xlabel('Date')
    axes[0, 0].set_ylabel('Humidity (%)')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # 2. Scatter plot
    axes[0, 1].scatter(test['humidity'], forecast_df['forecast'], alpha=0.6, s=50, color='blue')
    
    # Add perfect prediction line
    min_val = min(test['humidity'].min(), forecast_df['forecast'].min())
    max_val = max(test['humidity'].max(), forecast_df['forecast'].max())
    axes[0, 1].plot([min_val, max_val], [min_val, max_val], 
                    'r--', linewidth=2, label='Perfect Prediction')
    
    axes[0, 1].set_title('Actual vs Predicted (Scatter)', fontsize=12, fontweight='bold')
    axes[0, 1].set_xlabel('Actual Humidity (%)')
    axes[0, 1].set_ylabel('Predicted Humidity (%)')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    
    # 3. Prediction errors over time
    errors = test['humidity'].values - forecast_df['forecast'].values
    axes[1, 0].plot(test.index, errors, color='purple', linewidth=1, marker='o', markersize=3)
    axes[1, 0].axhline(y=0, color='red', linestyle='--', linewidth=2)
    axes[1, 0].axhline(y=errors.mean(), color='orange', linestyle='--', 
                       linewidth=1.5, label=f'Mean Error: {errors.mean():.2f}')
    axes[1, 0].fill_between(test.index, 0, errors, alpha=0.3, color='purple')
    axes[1, 0].set_title('Prediction Errors Over Time', fontsize=12, fontweight='bold')
    axes[1, 0].set_xlabel('Date')
    axes[1, 0].set_ylabel('Error (Actual - Predicted)')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    
    # 4. Error distribution
    axes[1, 1].hist(errors, bins=30, edgecolor='black', color='coral', alpha=0.7)
    axes[1, 1].axvline(errors.mean(), color='red', linestyle='--', 
                       linewidth=2, label=f'Mean: {errors.mean():.2f}')
    axes[1, 1].axvline(0, color='green', linestyle='--', 
                       linewidth=2, label='Zero Error')
    axes[1, 1].set_title('Distribution of Prediction Errors', fontsize=12, fontweight='bold')
    axes[1, 1].set_xlabel('Prediction Error')
    axes[1, 1].set_ylabel('Frequency')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('outputs/visualizations/arima_evaluation_plots.png', dpi=300, bbox_inches='tight')
    logger.info("Saved: arima_evaluation_plots.png")
    plt.show()

def create_metrics_summary(metrics):
    """Create and save metrics summary table"""
    metrics_df = pd.DataFrame({
        'Metric': list(metrics.keys()),
        'Value': [f"{v:.4f}" if isinstance(v, float) else v for v in metrics.values()]
    })
    
    metrics_df.to_csv('outputs/metrics/arima_evaluation_metrics.csv', index=False)
    logger.info("[SUCCESS] Metrics saved to arima_evaluation_metrics.csv")

def main():
    """Main evaluation pipeline"""
    logger.info("Starting ARIMA Model Evaluation...")
    
    # Load data
    test, forecast_df = load_data()
    if test is None or forecast_df is None:
        return
    
    # Ensure alignment
    test = test.head(len(forecast_df))
    
    logger.info(f"Evaluating {len(test)} predictions")
    
    # Calculate metrics
    metrics = calculate_metrics(test['humidity'], forecast_df['forecast'])
    
    # Print report
    print_metrics_report(metrics)
    
    # Create visualizations
    logger.info("\nGenerating evaluation plots...")
    plot_predictions_vs_actual(test, forecast_df)
    
    # Save metrics
    create_metrics_summary(metrics)
    
    logger.info("\n[SUCCESS] ARIMA evaluation completed successfully!")
    logger.info("\nGenerated files:")
    logger.info("  - arima_evaluation_plots.png")
    logger.info("  - arima_evaluation_metrics.csv")

if __name__ == "__main__":
    main()
