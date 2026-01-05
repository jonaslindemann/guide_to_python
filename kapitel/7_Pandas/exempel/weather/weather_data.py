#!/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides functionality to download and process weather data from NOAA's Global Summary of the Month (GSOM) dataset.
It simulates downloading weather data for various cities based on NOAA station IDs and generates realistic weather data.
"""

import pandas as pd
import numpy as np

def download_weather_data(station_ids, start_date, end_date):
    """
    Ladda ner väderdata från NOAA:s Global Summary of the Month (GSOM) dataset
    
    Parameters:
    station_ids: list of NOAA station IDs
    start_date: start date in YYYY-MM-DD format
    end_date: end date in YYYY-MM-DD format
    """
    
    # NOAA API endpoint for Global Summary of the Month
    base_url = "https://www.ncei.noaa.gov/data/global-summary-of-the-month/access/"
    
    all_data = []
    
    for station_id in station_ids:
        print(f"Laddar ner data för station: {station_id}")
        
        # For demonstration, we'll create sample data that mimics NOAA format
        # In practice, you would use actual NOAA API calls
        dates = pd.date_range(start=start_date, end=end_date, freq='MS')
        
        # Generate realistic weather data for different cities
        np.random.seed(hash(station_id) % 1000)  # Consistent data per station
        
        if 'NYC' in station_id:
            base_temp = 55  # NYC average
            precip_base = 3.5
        elif 'MIA' in station_id:
            base_temp = 75  # Miami average
            precip_base = 4.2
        elif 'DEN' in station_id:
            base_temp = 50  # Denver average
            precip_base = 1.8
        else:
            base_temp = 60
            precip_base = 3.0
            
        station_data = []
        for date in dates:
            # Seasonal temperature variation
            seasonal_temp = base_temp + 20 * np.sin(2 * np.pi * (date.month - 1) / 12)
            temp = seasonal_temp + np.random.normal(0, 5)
            
            # Seasonal precipitation variation
            seasonal_precip = precip_base * (1 + 0.3 * np.sin(2 * np.pi * (date.month - 1) / 12))
            precip = max(0, seasonal_precip + np.random.normal(0, 1))
            
            station_data.append({
                'STATION': station_id,
                'DATE': date.strftime('%Y-%m-%d'),
                'TAVG': round(temp, 1),  # Average temperature
                'TMAX': round(temp + np.random.uniform(5, 15), 1),  # Max temperature
                'TMIN': round(temp - np.random.uniform(5, 15), 1),  # Min temperature
                'PRCP': round(precip, 2),  # Precipitation
                'AWND': round(abs(np.random.normal(8, 3)), 1)  # Wind speed
            })
        
        all_data.extend(station_data)

    return convert_to_millimeters(convert_to_celcius(clean_weather_data(pd.DataFrame(all_data))))

def clean_weather_data(weather_df):

    # Konvertera datum till datetime och extrahera år och månad
    weather_df['DATE'] = pd.to_datetime(weather_df['DATE'])
    weather_df['YEAR'] = weather_df['DATE'].dt.year
    weather_df['MONTH'] = weather_df['DATE'].dt.month
    weather_df['CITY'] = weather_df['STATION'].str.extract(r'_(\w+)$')[0]

    return weather_df

def convert_to_celcius(weather_df):
    """
    Konvertera temperaturer från Fahrenheit till Celsius
    """
    weather_df['TAVG'] = (weather_df['TAVG'] - 32) * 5.0 / 9.0
    weather_df['TMAX'] = (weather_df['TMAX'] - 32) * 5.0 / 9.0
    weather_df['TMIN'] = (weather_df['TMIN'] - 32) * 5.0 / 9.0

    return weather_df

def convert_to_millimeters(weather_df):
    """
    Konvertera nederbörd från tum till millimeter
    """
    weather_df['PRCP'] = weather_df['PRCP'] * 25.4  # 1 inch = 25.4 mm
    return weather_df
