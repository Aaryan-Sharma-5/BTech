"""
Data Collection Script - Humidity Data for Ghatkopar, Mumbai
Fetches historical humidity data from Open-Meteo API for time series analysis
"""

import requests
import pandas as pd
import logging
import os
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Ensure data directory exists
Path('data').mkdir(parents=True, exist_ok=True)

# Configuration
CONFIG = {
    'latitude': 19.0860,
    'longitude': 72.9090,
    'location': 'Ghatkopar, Mumbai',
    'start_year': 2023,
    'end_year': 2026,
    'output_file': 'data/ghatkopar_humidity_2023_2024.csv'
}

def fetch_humidity_data(year, latitude, longitude):
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": f"{year}-01-01",
        "end_date": f"{year}-12-31",
        "daily": "relative_humidity_2m_mean",
        "timezone": "Asia/Kolkata"
    }

    try:
        response = requests.get(url, params=params, timeout=30)
        logger.info(f"Fetching {year} — Status code: {response.status_code}")

        if response.status_code != 200:
            logger.error(f"Failed to fetch data for {year}: {response.text}")
            return None

        data = response.json()
        if "daily" not in data:
            logger.warning(f"No daily data available for year {year}")
            return None

        year_df = pd.DataFrame({
            "date": data["daily"]["time"],
            "humidity": data["daily"]["relative_humidity_2m_mean"]
        })
        
        logger.info(f"Successfully fetched {len(year_df)} records for {year}")
        return year_df

    except requests.exceptions.RequestException as e:
        logger.error(f"Network error while fetching {year}: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error for {year}: {e}")
        return None

def main():
    logger.info(f"Starting data collection for {CONFIG['location']}")
    logger.info(f"Coordinates: ({CONFIG['latitude']}, {CONFIG['longitude']})")
    
    all_data = []

    for year in range(CONFIG['start_year'], CONFIG['end_year']):
        year_df = fetch_humidity_data(year, CONFIG['latitude'], CONFIG['longitude'])
        if year_df is not None:
            all_data.append(year_df)

    if not all_data:
        logger.error("No data collected. Exiting.")
        return

    final_df = pd.concat(all_data, ignore_index=True)
    
    logger.info(f"Total records collected: {len(final_df)}")
    logger.info(f"Date range: {final_df['date'].min()} to {final_df['date'].max()}")
    logger.info(f"Missing humidity values: {final_df['humidity'].isna().sum()}")
    
    final_df.to_csv(CONFIG['output_file'], index=False)
    logger.info(f"Data saved to {CONFIG['output_file']}")
    
    print("\nSummary Statistics:")
    print(final_df['humidity'].describe())
    print("\nFirst 5 records:")
    print(final_df.head())

if __name__ == "__main__":
    main()
