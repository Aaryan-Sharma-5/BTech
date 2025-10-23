"""
Data Preprocessing Script
Cleans and prepares humidity data for time series analysis
Handles missing values, outliers, and ensures data quality
"""

import pandas as pd
import numpy as np
import logging
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Ensure required directories exist
Path('data').mkdir(parents=True, exist_ok=True)
Path('outputs/visualizations').mkdir(parents=True, exist_ok=True)

# Configuration
CONFIG = {
    'input_file': 'data/ghatkopar_humidity_2023_2024.csv',
    'output_file': 'data/cleaned_humidity.csv',
    'outlier_threshold': 3  # Standard deviations for outlier detection
}

def detect_outliers(df, column='humidity', threshold=3):
    """
    Detect outliers using Z-score method
    
    Args:
        df (pd.DataFrame): Input dataframe
        column (str): Column to check for outliers
        threshold (int): Z-score threshold
    
    Returns:
        pd.Series: Boolean series indicating outliers
    """
    z_scores = np.abs((df[column] - df[column].mean()) / df[column].std())
    return z_scores > threshold

def preprocess_humidity_data(input_file, output_file):
    """
    Main preprocessing function
    
    Args:
        input_file (str): Path to raw data file
        output_file (str): Path to save cleaned data
    """
    try:
        # Load dataset
        logger.info(f"Loading data from {input_file}")
        df = pd.read_csv(input_file)
        
        logger.info(f"Initial dataset shape: {df.shape}")
        logger.info(f"Columns: {df.columns.tolist()}")
        
    except FileNotFoundError:
        logger.error(f"File not found: {input_file}")
        logger.error("Please run 1)dataset.py first to collect data.")
        return
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        return

    # Convert date to datetime
    df['date'] = pd.to_datetime(df['date'])
    logger.info(f"Date range: {df['date'].min()} to {df['date'].max()}")

    # Sort by date
    df = df.sort_values(by='date').reset_index(drop=True)
    logger.info("Data sorted chronologically")

    # Check for missing values
    missing_count = df['humidity'].isna().sum()
    logger.info(f"Missing humidity values: {missing_count} ({missing_count/len(df)*100:.2f}%)")

    # Fill missing humidity values using forward fill
    if missing_count > 0:
        df['humidity'] = df['humidity'].ffill()
        # Use backward fill for any remaining NaN at the start
        df['humidity'] = df['humidity'].bfill()
        logger.info("Missing values filled using forward-fill and back-fill methods")

    # Detect outliers
    outliers = detect_outliers(df, 'humidity', CONFIG['outlier_threshold'])
    outlier_count = outliers.sum()
    logger.info(f"Outliers detected: {outlier_count} ({outlier_count/len(df)*100:.2f}%)")
    
    if outlier_count > 0:
        logger.info(f"Outlier values: {df.loc[outliers, 'humidity'].tolist()}")
        # Optional: Cap outliers instead of removing
        # df.loc[outliers, 'humidity'] = df['humidity'].median()

    # Check for duplicates
    duplicates = df.duplicated(subset=['date']).sum()
    if duplicates > 0:
        logger.warning(f"Duplicate dates found: {duplicates}")
        df = df.drop_duplicates(subset=['date'], keep='first')
        logger.info("Duplicate dates removed")

    # Ensure no negative humidity values
    negative_values = (df['humidity'] < 0).sum()
    if negative_values > 0:
        logger.warning(f"Negative humidity values found: {negative_values}")
        df.loc[df['humidity'] < 0, 'humidity'] = 0

    # Ensure humidity is within 0-100% range
    over_100 = (df['humidity'] > 100).sum()
    if over_100 > 0:
        logger.warning(f"Humidity values over 100%: {over_100}")
        df.loc[df['humidity'] > 100, 'humidity'] = 100

    # Display statistics
    logger.info("\n📊 Cleaned Data Statistics:")
    logger.info(f"\n{df['humidity'].describe()}")

    # Save cleaned data
    df.to_csv(output_file, index=False)
    logger.info(f"✅ Cleaned data saved to {output_file}")
    
    # Create quality report visualization
    create_quality_report(df)

def create_quality_report(df):
    """
    Create visualization showing data quality metrics
    
    Args:
        df (pd.DataFrame): Cleaned dataframe
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Time series plot
    axes[0, 0].plot(df['date'], df['humidity'], linewidth=0.8, color='blue')
    axes[0, 0].set_title('Humidity Over Time (Cleaned)', fontsize=12, fontweight='bold')
    axes[0, 0].set_xlabel('Date')
    axes[0, 0].set_ylabel('Humidity (%)')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Distribution plot
    axes[0, 1].hist(df['humidity'], bins=50, color='skyblue', edgecolor='black', alpha=0.7)
    axes[0, 1].axvline(df['humidity'].mean(), color='red', linestyle='--', 
                       label=f"Mean: {df['humidity'].mean():.2f}%")
    axes[0, 1].axvline(df['humidity'].median(), color='green', linestyle='--', 
                       label=f"Median: {df['humidity'].median():.2f}%")
    axes[0, 1].set_title('Humidity Distribution', fontsize=12, fontweight='bold')
    axes[0, 1].set_xlabel('Humidity (%)')
    axes[0, 1].set_ylabel('Frequency')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    
    # Box plot
    axes[1, 0].boxplot(df['humidity'], vert=True, patch_artist=True,
                       boxprops=dict(facecolor='lightblue'))
    axes[1, 0].set_title('Humidity Box Plot (Outlier Detection)', fontsize=12, fontweight='bold')
    axes[1, 0].set_ylabel('Humidity (%)')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Summary statistics table
    axes[1, 1].axis('tight')
    axes[1, 1].axis('off')
    stats_data = [
        ['Metric', 'Value'],
        ['Count', f"{len(df)}"],
        ['Mean', f"{df['humidity'].mean():.2f}%"],
        ['Std Dev', f"{df['humidity'].std():.2f}%"],
        ['Min', f"{df['humidity'].min():.2f}%"],
        ['25%', f"{df['humidity'].quantile(0.25):.2f}%"],
        ['Median', f"{df['humidity'].median():.2f}%"],
        ['75%', f"{df['humidity'].quantile(0.75):.2f}%"],
        ['Max', f"{df['humidity'].max():.2f}%"]
    ]
    table = axes[1, 1].table(cellText=stats_data, cellLoc='left', loc='center',
                             colWidths=[0.4, 0.4])
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 2)
    axes[1, 1].set_title('Summary Statistics', fontsize=12, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('outputs/visualizations/data_quality_report.png', dpi=300, bbox_inches='tight')
    logger.info("Data quality report saved as 'outputs/visualizations/data_quality_report.png'")
    plt.show()

if __name__ == "__main__":
    preprocess_humidity_data(CONFIG['input_file'], CONFIG['output_file'])
