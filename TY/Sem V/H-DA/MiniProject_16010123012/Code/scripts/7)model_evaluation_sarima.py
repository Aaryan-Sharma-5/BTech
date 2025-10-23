"""
Comprehensive Model Comparison Script
Compares ARIMA vs SARIMA performance with:
- Multiple error metrics (MAE, RMSE, MAPE, R²)
- Side-by-side visualizations
- Statistical comparison tests
- Recommendation for best model
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

def load_all_data():
    """Load actual test data and both model forecasts"""
    try:
        # Load actual data
        df = pd.read_csv("data/cleaned_humidity.csv")
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)
        
        train_size = int(len(df) * 0.8)
        test = df[train_size:]
        
        # Load ARIMA forecast
        forecast_arima = pd.read_csv("data/forecast_results.csv")
        forecast_arima['date'] = pd.to_datetime(forecast_arima['date'])
        forecast_arima.set_index('date', inplace=True)
        
        # Load SARIMA forecast
        forecast_sarima = pd.read_csv("data/forecast_results_sarima.csv")
        forecast_sarima['date'] = pd.to_datetime(forecast_sarima['date'])
        forecast_sarima.set_index('date', inplace=True)
        
        logger.info("[SUCCESS] All data loaded successfully")
        return test, forecast_arima, forecast_sarima
        
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        logger.error("Please run forecasting scripts (4 and 6) first")
        return None, None, None

def calculate_all_metrics(actual, predicted, model_name):
    """Calculate comprehensive metrics for a model"""
    mae = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    mape = mean_absolute_percentage_error(actual, predicted) * 100
    r2 = r2_score(actual, predicted)
    
    # Normalized RMSE
    nrmse = rmse / (actual.max() - actual.min()) * 100
    
    metrics = {
        'Model': model_name,
        'MAE': mae,
        'RMSE': rmse,
        'NRMSE (%)': nrmse,
        'MAPE (%)': mape,
        'R² Score': r2
    }
    
    return metrics

def print_comparison_report(metrics_arima, metrics_sarima):
    """Print detailed comparison report"""
    print("\n" + "="*80)
    print("[COMPARISON] MODEL COMPARISON: ARIMA vs SARIMA")
    print("="*80)
    
    print(f"\n{'Metric':<20} {'ARIMA':<20} {'SARIMA':<20} {'Winner'}")
    print("-"*80)
    
    # Compare each metric
    metrics_to_compare = ['MAE', 'RMSE', 'NRMSE (%)', 'MAPE (%)']
    winners = []
    
    for metric in metrics_to_compare:
        arima_val = metrics_arima[metric]
        sarima_val = metrics_sarima[metric]
        
        # Lower is better for these metrics
        if sarima_val < arima_val:
            winner = "[WINNER] SARIMA"
            winners.append('SARIMA')
            improvement = ((arima_val - sarima_val) / arima_val) * 100
        else:
            winner = "[WINNER] ARIMA"
            winners.append('ARIMA')
            improvement = ((sarima_val - arima_val) / sarima_val) * 100
        
        print(f"{metric:<20} {arima_val:<20.4f} {sarima_val:<20.4f} {winner} ({improvement:.1f}% better)")
    
    # R² Score (higher is better)
    r2_arima = metrics_arima['R² Score']
    r2_sarima = metrics_sarima['R² Score']
    
    if r2_sarima > r2_arima:
        r2_winner = "[WINNER] SARIMA"
        winners.append('SARIMA')
    else:
        r2_winner = "[WINNER] ARIMA"
        winners.append('ARIMA')
    
    print(f"{'R² Score':<20} {r2_arima:<20.4f} {r2_sarima:<20.4f} {r2_winner}")
    
    print("="*80)
    
    # Overall recommendation
    print("\n[RECOMMENDATION] OVERALL RECOMMENDATION:")
    sarima_wins = winners.count('SARIMA')
    arima_wins = winners.count('ARIMA')
    
    if sarima_wins > arima_wins:
        print(f"   [BEST] SARIMA is the better model ({sarima_wins}/{len(winners)} metrics)")
        print("   Status: SARIMA better captures seasonal patterns in humidity data")
        best_model = 'SARIMA'
    elif arima_wins > sarima_wins:
        print(f"   [BEST] ARIMA is the better model ({arima_wins}/{len(winners)} metrics)")
        print("   → Simpler ARIMA model is sufficient for this data")
        best_model = 'ARIMA'
    else:
        print("   ⚖ Models perform similarly - consider computational cost")
        best_model = 'TIE'
    
    print("="*80)
    
    return best_model

def plot_side_by_side_comparison(test, forecast_arima, forecast_sarima):
    """Create comprehensive side-by-side comparison plots"""
    fig = plt.figure(figsize=(18, 12))
    gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)
    
    # 1. Time series comparison - ARIMA
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.plot(test.index, test['humidity'], label='Actual', 
             color='green', linewidth=2, alpha=0.7)
    ax1.plot(forecast_arima.index, forecast_arima['forecast'], 
             label='ARIMA Forecast', color='red', linewidth=2, alpha=0.7)
    
    if 'lower_ci' in forecast_arima.columns:
        ax1.fill_between(forecast_arima.index, 
                         forecast_arima['lower_ci'], 
                         forecast_arima['upper_ci'], 
                         color='red', alpha=0.2)
    
    ax1.set_title('ARIMA: Actual vs Predicted', fontsize=12, fontweight='bold')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Humidity (%)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. Time series comparison - SARIMA
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.plot(test.index, test['humidity'], label='Actual', 
             color='green', linewidth=2, alpha=0.7)
    ax2.plot(forecast_sarima.index, forecast_sarima['forecast'], 
             label='SARIMA Forecast', color='blue', linewidth=2, alpha=0.7)
    
    if 'lower_ci' in forecast_sarima.columns:
        ax2.fill_between(forecast_sarima.index, 
                         forecast_sarima['lower_ci'], 
                         forecast_sarima['upper_ci'], 
                         color='blue', alpha=0.2)
    
    ax2.set_title('SARIMA: Actual vs Predicted', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Humidity (%)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # 3. Scatter plots
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.scatter(test['humidity'], forecast_arima['forecast'], 
                alpha=0.6, s=50, color='red', label='ARIMA')
    min_val = test['humidity'].min()
    max_val = test['humidity'].max()
    ax3.plot([min_val, max_val], [min_val, max_val], 
             'k--', linewidth=2, label='Perfect Prediction')
    ax3.set_title('ARIMA: Actual vs Predicted Scatter', fontsize=12, fontweight='bold')
    ax3.set_xlabel('Actual Humidity (%)')
    ax3.set_ylabel('Predicted Humidity (%)')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.scatter(test['humidity'], forecast_sarima['forecast'], 
                alpha=0.6, s=50, color='blue', label='SARIMA')
    ax4.plot([min_val, max_val], [min_val, max_val], 
             'k--', linewidth=2, label='Perfect Prediction')
    ax4.set_title('SARIMA: Actual vs Predicted Scatter', fontsize=12, fontweight='bold')
    ax4.set_xlabel('Actual Humidity (%)')
    ax4.set_ylabel('Predicted Humidity (%)')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    # 5. Error comparison
    ax5 = fig.add_subplot(gs[2, 0])
    errors_arima = test['humidity'].values - forecast_arima['forecast'].values
    errors_sarima = test['humidity'].values - forecast_sarima['forecast'].values
    
    ax5.plot(test.index, errors_arima, label='ARIMA Errors', 
             color='red', linewidth=1.5, alpha=0.7)
    ax5.plot(test.index, errors_sarima, label='SARIMA Errors', 
             color='blue', linewidth=1.5, alpha=0.7)
    ax5.axhline(y=0, color='black', linestyle='--', linewidth=2)
    ax5.set_title('Prediction Errors Comparison', fontsize=12, fontweight='bold')
    ax5.set_xlabel('Date')
    ax5.set_ylabel('Error (Actual - Predicted)')
    ax5.legend()
    ax5.grid(True, alpha=0.3)
    
    # 6. Error distribution comparison
    ax6 = fig.add_subplot(gs[2, 1])
    ax6.hist(errors_arima, bins=20, alpha=0.5, color='red', 
             label=f'ARIMA (std={errors_arima.std():.2f})', edgecolor='black')
    ax6.hist(errors_sarima, bins=20, alpha=0.5, color='blue', 
             label=f'SARIMA (std={errors_sarima.std():.2f})', edgecolor='black')
    ax6.axvline(0, color='black', linestyle='--', linewidth=2)
    ax6.set_title('Error Distribution Comparison', fontsize=12, fontweight='bold')
    ax6.set_xlabel('Prediction Error')
    ax6.set_ylabel('Frequency')
    ax6.legend()
    ax6.grid(True, alpha=0.3)
    
    plt.savefig('outputs/visualizations/model_comparison_comprehensive.png', dpi=300, bbox_inches='tight')
    logger.info("Saved: model_comparison_comprehensive.png")
    plt.show()

def create_metrics_comparison_table(metrics_arima, metrics_sarima):
    """Create and save metrics comparison table"""
    comparison_df = pd.DataFrame([metrics_arima, metrics_sarima])
    
    # Calculate improvements
    improvement = {}
    for metric in ['MAE', 'RMSE', 'NRMSE (%)', 'MAPE (%)']:
        diff = metrics_arima[metric] - metrics_sarima[metric]
        pct = (diff / metrics_arima[metric]) * 100
        improvement[metric] = f"{pct:+.2f}%"
    
    improvement['R² Score'] = f"{(metrics_sarima['R² Score'] - metrics_arima['R² Score'])*100:+.2f}%"
    improvement['Model'] = 'SARIMA Improvement'
    
    improvement_df = pd.DataFrame([improvement])
    final_df = pd.concat([comparison_df, improvement_df], ignore_index=True)
    
    final_df.to_csv('outputs/metrics/model_comparison_metrics.csv', index=False)
    logger.info("[SUCCESS] Metrics comparison saved to model_comparison_metrics.csv")
    
    return final_df

def main():
    """Main model comparison pipeline"""
    logger.info("Starting Comprehensive Model Comparison...")
    
    # Load all data
    test, forecast_arima, forecast_sarima = load_all_data()
    if test is None:
        return
    
    # Align data lengths
    min_len = min(len(forecast_arima), len(forecast_sarima))
    test = test.head(min_len)
    forecast_arima = forecast_arima.head(min_len)
    forecast_sarima = forecast_sarima.head(min_len)
    
    logger.info(f"Comparing {len(test)} predictions")
    
    # Calculate metrics for both models
    metrics_arima = calculate_all_metrics(
        test['humidity'], 
        forecast_arima['forecast'], 
        'ARIMA'
    )
    
    metrics_sarima = calculate_all_metrics(
        test['humidity'], 
        forecast_sarima['forecast'], 
        'SARIMA'
    )
    
    # Print comparison report
    best_model = print_comparison_report(metrics_arima, metrics_sarima)
    
    # Create visualizations
    logger.info("\nGenerating comparison plots...")
    plot_side_by_side_comparison(test, forecast_arima, forecast_sarima)
    
    # Save comparison table
    comparison_df = create_metrics_comparison_table(metrics_arima, metrics_sarima)
    
    print("\n[TABLE] Full Metrics Comparison Table:")
    print(comparison_df.to_string(index=False))
    
    logger.info("\n[SUCCESS] Model comparison completed successfully!")
    logger.info("\nGenerated files:")
    logger.info("  - model_comparison_comprehensive.png")
    logger.info("  - model_comparison_metrics.csv")
    
    print(f"\n[RECOMMENDATION] Use {best_model} model for production deployment")

if __name__ == "__main__":
    main()
