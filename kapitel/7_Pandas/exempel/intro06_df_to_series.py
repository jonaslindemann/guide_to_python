import pandas as pd
import numpy as np

equipment_ids = ['Pump_001', 'Motor_002', 'Tank_003', 'Compressor_004', 'Valve_005']

temperatures = pd.Series([78.5, 82.1, 76.3, 85.2, 79.8], index=equipment_ids)
pressures = pd.Series([2.1, 1.8, 0.5, 8.2, 3.4], index=equipment_ids)
vibrations = pd.Series([0.8, 1.2, 0.3, 2.1, 0.6], index=equipment_ids)

equipment_df = pd.DataFrame({
    'temperature_c': temperatures,
    'pressure_bar': pressures,
    'vibration_mm_s': vibrations
})

# Extract a single column (returns a Series)
temp_series = equipment_df['temperature_c']
print("Extracted temperature Series:")
print(temp_series)
print(f"Type: {type(temp_series)}")
print()

# Extract multiple columns (returns a DataFrame)
temp_pressure_df = equipment_df[['temperature_c', 'pressure_bar']]
print("Extracted temperature and pressure (DataFrame):")
print(temp_pressure_df)
print(f"Type: {type(temp_pressure_df)}")
print()

# Extract a row (returns a Series)
pump_001_data = equipment_df.loc['Pump_001']
print("Pump_001 all measurements (Series):")
print(pump_001_data)
print(f"Type: {type(pump_001_data)}")
print()
