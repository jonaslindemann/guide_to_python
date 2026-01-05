import pandas as pd
import numpy as np
import sys

equipment_ids = ['Pump_001', 'Motor_002', 'Tank_003', 'Compressor_004', 'Valve_005']

temperatures = pd.Series([78.5, 82.1, 76.3, 85.2, 79.8], index=equipment_ids)
pressures = pd.Series([2.1, 1.8, 0.5, 8.2, 3.4], index=equipment_ids)
vibrations = pd.Series([0.8, 1.2, 0.3, 2.1, 0.6], index=equipment_ids)

equipment_df = pd.DataFrame({
    'temperature_c': temperatures,
    'pressure_bar': pressures,
    'vibration_mm_s': vibrations
})

print(equipment_df)

# Extract a single column (returns a Series)
temp_series = equipment_df['temperature_c']
print(temp_series)


# Extract multiple columns (returns a DataFrame)
temp_pressure_df = equipment_df[['temperature_c', 'pressure_bar']]
print(temp_pressure_df)

# Extract a row (returns a Series)
pump_001_data = equipment_df.loc['Pump_001']
print(pump_001_data)

motor_002_data = equipment_df.iloc[1]
print(motor_002_data)

compressor_pressure = equipment_df.loc['Compressor_004', 'pressure_bar']
print(compressor_pressure)




# Extract multiple rows (returns a DataFrame)
pumps_and_motors = equipment_df.loc[['Pump_001', 'Motor_002']]
print(pumps_and_motors)

hot_equipment_df = equipment_df[equipment_df['temperature_c'] > 80]
print(hot_equipment_df)

hot_or_high_pressure_df = equipment_df[(equipment_df['temperature_c'] > 80) | (equipment_df['pressure_bar'] > 5)]
print(hot_or_high_pressure_df)  

cool_equipment = equipment_df.query('temperature_c < 80')
print(cool_equipment)



sys.exit(0)  # Exit early for demonstration purposes

print(f"Type: {type(pumps_and_motors)}")

print()
# Extract a specific value (scalar)
pump_001_temp = equipment_df.at['Pump_001', 'temperature_c']

print("Pump_001 temperature (scalar):")
print(pump_001_temp)
print(f"Type: {type(pump_001_temp)}")

# Extract a specific value using .iat (integer location)
pump_001_temp_iat = equipment_df.iat[0, 0]  #
print("Pump_001 temperature using .iat (scalar):")
print(pump_001_temp_iat)
print(f"Type: {type(pump_001_temp_iat)}")

# Extract a specific value using .iloc (integer location)
pump_001_temp_iloc = equipment_df.iloc[0, 0]  # First row, first column
print("Pump_001 temperature using .iloc (scalar):")
print(pump_001_temp_iloc)
print(f"Type: {type(pump_001_temp_iloc)}")

# Extract a specific value using .loc (label-based)
pump_001_temp_loc = equipment_df.loc['Pump_001', 'temperature_c']   
print("Pump_001 temperature using .loc (scalar):")
print(pump_001_temp_loc)
print(f"Type: {type(pump_001_temp_loc)}")

# Extract a specific value using .at (label-based)
pump_001_temp_at = equipment_df.at['Pump_001', 'temperature_c'] 
print("Pump_001 temperature using .at (scalar):")
print(pump_001_temp_at)
print(f"Type: {type(pump_001_temp_at)}")

# Extract a specific value using .xs (cross-section)
pump_001_temp_xs = equipment_df.xs('Pump_001')['temperature_c']
print("Pump_001 temperature using .xs (scalar):")
print(pump_001_temp_xs)
print(f"Type: {type(pump_001_temp_xs)}")

# Extract a specific value using .get (label-based)
pump_001_temp_get = equipment_df.get('temperature_c').get('Pump_001')
print("Pump_001 temperature using .get (scalar):")
print(pump_001_temp_get)
print(f"Type: {type(pump_001_temp_get)}")

# Extract a specific value using .query (label-based)
pump_001_temp_query = equipment_df.query("index == 'Pump_001'")['temperature_c'].values[0]
print("Pump_001 temperature using .query (scalar):")
print(pump_001_temp_query)
print(f"Type: {type(pump_001_temp_query)}")

# Extract a specific value using .filter (label-based)
pump_001_temp_filter = equipment_df.filter(items=['Pump_001'], axis=0)['temperature_c'].values[0]
print("Pump_001 temperature using .filter (scalar):")
print(pump_001_temp_filter)
print(f"Type: {type(pump_001_temp_filter)}")

# Extract a specific value using .iloc with a boolean mask
pump_001_temp_mask = equipment_df.iloc[(equipment_df.index == 'Pump_001').argmax(), 0]
print("Pump_001 temperature using boolean mask with .iloc (scalar):")
print(pump_001_temp_mask)
print(f"Type: {type(pump_001_temp_mask)}")

# Extract a specific value using .loc with a boolean mask
pump_001_temp_mask_loc = equipment_df.loc[equipment_df.index == 'Pump_001', 'temperature_c'].values[0]
print("Pump_001 temperature using boolean mask with .loc (scalar):")
print(pump_001_temp_mask_loc)
print(f"Type: {type(pump_001_temp_mask_loc)}")

# Extract a specific value using .iat with a boolean mask
pump_001_temp_mask_iat = equipment_df.iat[(equipment_df.index == 'Pump_001').argmax(), 0]
print("Pump_001 temperature using boolean mask with .iat (scalar):")
print(pump_001_temp_mask_iat)
print(f"Type: {type(pump_001_temp_mask_iat)}")

# Extract a specific value using .at with a boolean mask
pump_001_temp_mask_at = equipment_df.at[equipment_df.index[(equipment_df.index == 'Pump_001').argmax()], 'temperature_c']
print("Pump_001 temperature using boolean mask with .at (scalar):") 
print(pump_001_temp_mask_at)
print(f"Type: {type(pump_001_temp_mask_at)}")

# Extract a specific value using .xs with a boolean mask
pump_001_temp_mask_xs = equipment_df.xs(equipment_df.index[(equipment_df.index == 'Pump_001').argmax()])['temperature_c']
print("Pump_001 temperature using boolean mask with .xs (scalar):") 
