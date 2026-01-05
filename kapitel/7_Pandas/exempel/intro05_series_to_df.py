import pandas as pd
import numpy as np

equipment_ids = ['Pump_001', 'Motor_002', 'Tank_003', 'Compressor_004', 'Valve_005']

temperatures = pd.Series([78.5, 82.1, 76.3, 85.2, 79.8], index=equipment_ids)
pressures = pd.Series([2.1, 1.8, 0.5, 8.2, 3.4], index=equipment_ids)
vibrations = pd.Series([0.8, 1.2, 0.3, 2.1, 0.6], index=equipment_ids)

print("Temperature Series:")
print(temperatures)
print("\nPressure Series:")
print(pressures)
print("\nVibration Series:")
print(vibrations)
print()

# Combine Series into DataFrame
print("Combining Series into a DataFrame:")
equipment_df = pd.DataFrame({
    'temperature_c': temperatures,
    'pressure_bar': pressures,
    'vibration_mm_s': vibrations
})

print(equipment_df)
print()

# Show the relationship
print("Understanding the relationship:")
print("DataFrame is essentially a collection of Series with a common index")
print("Kolumnnamn:", equipment_df.columns)
print("Antal rader:", len(equipment_df))
print("Antal kolumner:", len(equipment_df.columns))
print("DataFrame shape:", equipment_df.shape)
print("DataFrame-datatyper:", equipment_df.dtypes)
print()