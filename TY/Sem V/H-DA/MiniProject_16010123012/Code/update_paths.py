"""
Script to update all file paths in the Python scripts to match new folder structure
"""

import re
from pathlib import Path

# Define path mappings (old -> new)
PATH_MAPPINGS = {
    # CSV files (data) - Change from ../ to direct paths
    "'../data/ghatkopar_humidity_2023_2024.csv'": "'data/ghatkopar_humidity_2023_2024.csv'",
    '"../data/ghatkopar_humidity_2023_2024.csv"': '"data/ghatkopar_humidity_2023_2024.csv"',
    "'../data/cleaned_humidity.csv'": "'data/cleaned_humidity.csv'",
    '"../data/cleaned_humidity.csv"': '"data/cleaned_humidity.csv"',
    "'../data/forecast_results.csv'": "'data/forecast_results.csv'",
    '"../data/forecast_results.csv"': '"data/forecast_results.csv"',
    "'../data/forecast_results_sarima.csv'": "'data/forecast_results_sarima.csv'",
    '"../data/forecast_results_sarima.csv"': '"data/forecast_results_sarima.csv"',
    
    # Metrics files - Change from ../ to direct paths
    "'../outputs/metrics/arima_evaluation_metrics.csv'": "'outputs/metrics/arima_evaluation_metrics.csv'",
    '"../outputs/metrics/arima_evaluation_metrics.csv"': '"outputs/metrics/arima_evaluation_metrics.csv"',
    "'../outputs/metrics/model_comparison_metrics.csv'": "'outputs/metrics/model_comparison_metrics.csv'",
    '"../outputs/metrics/model_comparison_metrics.csv"': '"outputs/metrics/model_comparison_metrics.csv"',
    "'../outputs/metrics/arima_parameter_search_results.csv'": "'outputs/metrics/arima_parameter_search_results.csv'",
    '"../outputs/metrics/arima_parameter_search_results.csv"': '"outputs/metrics/arima_parameter_search_results.csv"',
    "'../outputs/metrics/sarima_parameter_search_results.csv'": "'outputs/metrics/sarima_parameter_search_results.csv'",
    '"../outputs/metrics/sarima_parameter_search_results.csv"': '"outputs/metrics/sarima_parameter_search_results.csv"',
    
    # PNG files (visualizations) - Change from ../ to direct paths
    "'../outputs/visualizations/humidity_trend.png'": "'outputs/visualizations/humidity_trend.png'",
    '"../outputs/visualizations/humidity_trend.png"': '"outputs/visualizations/humidity_trend.png"',
    "'../outputs/visualizations/monthly_humidity.png'": "'outputs/visualizations/monthly_humidity.png'",
    '"../outputs/visualizations/monthly_humidity.png"': '"outputs/visualizations/monthly_humidity.png"',
    "'../outputs/visualizations/acf_pacf_plots.png'": "'outputs/visualizations/acf_pacf_plots.png'",
    '"../outputs/visualizations/acf_pacf_plots.png"': '"outputs/visualizations/acf_pacf_plots.png"',
    "'../outputs/visualizations/seasonal_decomposition.png'": "'outputs/visualizations/seasonal_decomposition.png'",
    '"../outputs/visualizations/seasonal_decomposition.png"': '"outputs/visualizations/seasonal_decomposition.png"',
    "'../outputs/visualizations/yearly_comparison.png'": "'outputs/visualizations/yearly_comparison.png'",
    '"../outputs/visualizations/yearly_comparison.png"': '"outputs/visualizations/yearly_comparison.png"',
    "'../outputs/visualizations/data_quality_report.png'": "'outputs/visualizations/data_quality_report.png'",
    '"../outputs/visualizations/data_quality_report.png"': '"outputs/visualizations/data_quality_report.png"',
    "'../outputs/visualizations/arima_residual_analysis.png'": "'outputs/visualizations/arima_residual_analysis.png'",
    '"../outputs/visualizations/arima_residual_analysis.png"': '"outputs/visualizations/arima_residual_analysis.png"',
    "'../outputs/visualizations/arima_forecast_with_confidence.png'": "'outputs/visualizations/arima_forecast_with_confidence.png'",
    '"../outputs/visualizations/arima_forecast_with_confidence.png"': '"outputs/visualizations/arima_forecast_with_confidence.png"',
    "'../outputs/visualizations/arima_evaluation_plots.png'": "'outputs/visualizations/arima_evaluation_plots.png'",
    '"../outputs/visualizations/arima_evaluation_plots.png"': '"outputs/visualizations/arima_evaluation_plots.png"',
    "'../outputs/visualizations/sarima_seasonality_check.png'": "'outputs/visualizations/sarima_seasonality_check.png'",
    '"../outputs/visualizations/sarima_seasonality_check.png"': '"outputs/visualizations/sarima_seasonality_check.png"',
    "'../outputs/visualizations/sarima_residual_analysis.png'": "'outputs/visualizations/sarima_residual_analysis.png'",
    '"../outputs/visualizations/sarima_residual_analysis.png"': '"outputs/visualizations/sarima_residual_analysis.png"',
    "'../outputs/visualizations/sarima_forecast_with_confidence.png'": "'outputs/visualizations/sarima_forecast_with_confidence.png'",
    '"../outputs/visualizations/sarima_forecast_with_confidence.png"': '"outputs/visualizations/sarima_forecast_with_confidence.png"',
    "'../outputs/visualizations/model_comparison_comprehensive.png'": "'outputs/visualizations/model_comparison_comprehensive.png'",
    '"../outputs/visualizations/model_comparison_comprehensive.png"': '"outputs/visualizations/model_comparison_comprehensive.png"',
}

def update_script_paths(script_path):
    """Update file paths in a single script"""
    print(f"\nProcessing: {script_path}")
    
    # Read the file
    with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    replacements_made = 0
    
    # Apply all path mappings
    for old_path, new_path in PATH_MAPPINGS.items():
        if old_path in content:
            content = content.replace(old_path, new_path)
            replacements_made += 1
            print(f"  ✓ Replaced: {old_path} -> {new_path}")
    
    # Write back if changes were made
    if content != original_content:
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ Updated {replacements_made} path(s) in {script_path.name}")
    else:
        print(f"  ℹ No changes needed for {script_path.name}")
    
    return replacements_made

def main():
    """Main function to update all scripts"""
    print("="*70)
    print("UPDATING SCRIPT PATHS FOR NEW FOLDER STRUCTURE")
    print("="*70)
    
    scripts_dir = Path('scripts')
    python_files = list(scripts_dir.glob('*.py'))
    
    if not python_files:
        print("❌ No Python files found in scripts directory!")
        return
    
    print(f"\nFound {len(python_files)} Python file(s) to update")
    
    total_replacements = 0
    for script in python_files:
        replacements = update_script_paths(script)
        total_replacements += replacements
    
    print("\n" + "="*70)
    print(f"✅ COMPLETE! Made {total_replacements} total path replacements")
    print("="*70)
    print("\nNew folder structure:")
    print("  📁 data/           - All CSV data files")
    print("  📁 scripts/        - All Python scripts")
    print("  📁 outputs/")
    print("    📁 visualizations/ - All PNG plots")
    print("    📁 metrics/        - All metrics CSV files")
    print("    📁 models/         - Model artifacts (future use)")
    print("  📁 docs/           - Documentation files")
    print("  📄 run_pipeline.py - Main execution script")
    print("  📄 config.py       - Centralized configuration")

if __name__ == "__main__":
    main()
