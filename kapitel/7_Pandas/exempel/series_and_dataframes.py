import pandas as pd
import numpy as np

# ============================================================================
# PART 1: UNDERSTANDING PANDAS SERIES
# ============================================================================

print("=== PART 1: UNDERSTANDING PANDAS SERIES ===")
print()

# What is a Series? Think of it as a single column of data with an index
print("1. Creating a Series - Temperature readings from a sensor")
print("-" * 50)

# Create a Series from a list - temperature readings
temperatures = pd.Series([22.5, 23.1, 24.8, 23.9, 22.2])
print("Basic temperature Series:")
print(temperatures)
print(f"Data type: {type(temperatures)}")
print()

# Series has two main components: values and index
print("Series components:")
print(f"Values: {temperatures.values}")
print(f"Values type: {type(temperatures.values)}")  # numpy array!
print(f"Index: {temperatures.index}")
print(f"Index type: {type(temperatures.index)}")
print()

# ============================================================================
# PART 2: SERIES WITH CUSTOM INDEX
# ============================================================================

print("2. Series with meaningful index - Equipment measurements")
print("-" * 50)

# Create Series with custom index (equipment IDs)
equipment_temps = pd.Series(
    data=[78.5, 82.1, 76.3, 85.2, 79.8],
    index=['Pump_001', 'Motor_002', 'Tank_003', 'Compressor_004', 'Valve_005']
)

print("Equipment temperature readings:")
print(equipment_temps)
print()

# Access data by index label (like a dictionary)
print("Accessing data by equipment ID:")
print(f"Pump_001 temperature: {equipment_temps['Pump_001']}°C")
print(f"Motor_002 temperature: {equipment_temps['Motor_002']}°C")
print()

# Access multiple equipment
print("Multiple equipment temperatures:")
pumps_and_motors = equipment_temps[['Pump_001', 'Motor_002']]
print(pumps_and_motors)
print()

# ============================================================================
# PART 3: SERIES OPERATIONS
# ============================================================================

print("3. Series operations - Engineering calculations")
print("-" * 50)

# Mathematical operations on entire Series
print("Converting Celsius to Fahrenheit:")
equipment_temps_f = equipment_temps * 9/5 + 32
print(equipment_temps_f)
print()

# Boolean operations - finding equipment above threshold
print("Equipment above 80°C:")
hot_equipment = equipment_temps > 80
print(hot_equipment)
print()

print("Which equipment is running hot:")
overheated = equipment_temps[equipment_temps > 80]
print(overheated)
print()

# Statistical operations
print("Temperature statistics:")
print(f"Mean temperature: {equipment_temps.mean():.2f}°C")
print(f"Max temperature: {equipment_temps.max():.2f}°C")
print(f"Min temperature: {equipment_temps.min():.2f}°C")
print(f"Standard deviation: {equipment_temps.std():.2f}°C")
print()

# ============================================================================
# PART 4: SERIES WITH TIME INDEX
# ============================================================================

print("4. Series with time index - Process monitoring")
print("-" * 50)

# Create time-indexed Series
time_index = pd.date_range('2024-01-01 08:00', periods=24, freq='1H')
reactor_pressure = pd.Series(
    data=np.random.normal(5.2, 0.3, 24),  # 5.2 bar average, 0.3 std
    index=time_index
)

print("24-hour reactor pressure monitoring:")
print(reactor_pressure.head(10))  # Show first 10 hours
print("...")
print(reactor_pressure.tail(3))   # Show last 3 hours
print()

# Time-based operations
print("Pressure during business hours (9 AM - 5 PM):")
business_hours = reactor_pressure.between_time('09:00', '17:00')
print(business_hours)
print()

# ============================================================================
# PART 5: FROM SERIES TO DATAFRAMES
# ============================================================================

print("=== PART 5: FROM SERIES TO DATAFRAMES ===")
print()

print("5. How Series combine to form DataFrames")
print("-" * 50)

# Create multiple Series for the same equipment
print("Individual Series for different measurements:")

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
print(f"DataFrame shape: {equipment_df.shape}")
print(f"DataFrame columns: {list(equipment_df.columns)}")
print(f"DataFrame index: {list(equipment_df.index)}")
print()

# ============================================================================
# PART 6: EXTRACTING SERIES FROM DATAFRAMES
# ============================================================================

print("6. Extracting Series from DataFrames")
print("-" * 50)

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

# ============================================================================
# PART 7: SERIES ALIGNMENT AND OPERATIONS
# ============================================================================

print("7. Series alignment - The magic behind DataFrame operations")
print("-" * 50)

# Create two Series with different indices
morning_temps = pd.Series([75.2, 76.8, 78.1], index=['Pump_001', 'Motor_002', 'Tank_003'])
evening_temps = pd.Series([79.5, 81.2, 77.9, 80.1], index=['Motor_002', 'Tank_003', 'Compressor_004', 'Valve_005'])

print("Morning temperatures:")
print(morning_temps)
print("\nEvening temperatures:")
print(evening_temps)
print()

# Series automatically align on index during operations
print("Temperature change (Evening - Morning):")
temp_change = evening_temps - morning_temps
print(temp_change)
print("Note: Only matching equipment IDs are calculated, others become NaN")
print()

# This is exactly what happens inside DataFrames!
print("This alignment behavior is what makes DataFrame operations work:")
print("When you do df['col1'] + df['col2'], pandas aligns the Series by index")
print()

# ============================================================================
# PART 8: PRACTICAL ENGINEERING EXAMPLES
# ============================================================================

print("8. Practical engineering examples with Series")
print("-" * 50)

# Example 1: Sensor calibration
print("Example 1: Sensor calibration")
raw_readings = pd.Series([1.23, 2.45, 3.67, 4.89, 6.11], 
                        index=['Sensor_A', 'Sensor_B', 'Sensor_C', 'Sensor_D', 'Sensor_E'])

# Calibration factors for each sensor
calibration_factors = pd.Series([0.98, 1.02, 0.99, 1.01, 0.97],
                               index=['Sensor_A', 'Sensor_B', 'Sensor_C', 'Sensor_D', 'Sensor_E'])

calibrated_readings = raw_readings * calibration_factors

print("Raw readings:")
print(raw_readings)
print("\nCalibration factors:")
print(calibration_factors)
print("\nCalibrated readings:")
print(calibrated_readings)
print()

# Example 2: Equipment efficiency calculation
print("Example 2: Equipment efficiency calculation")
actual_output = pd.Series([95, 88, 102, 78, 115], 
                         index=['Line_A', 'Line_B', 'Line_C', 'Line_D', 'Line_E'])
design_output = pd.Series([100, 90, 100, 80, 120],
                         index=['Line_A', 'Line_B', 'Line_C', 'Line_D', 'Line_E'])

efficiency = (actual_output / design_output) * 100

print("Actual output:")
print(actual_output)
print("\nDesign output:")
print(design_output)
print("\nEfficiency (%):")
print(efficiency.round(1))
print()

# Example 3: Alarm conditions
print("Example 3: Identifying alarm conditions")
current_pressures = pd.Series([5.2, 8.7, 3.1, 6.8, 9.2],
                             index=['Vessel_1', 'Vessel_2', 'Vessel_3', 'Vessel_4', 'Vessel_5'])
max_pressures = pd.Series([6.0, 8.0, 4.0, 7.0, 9.0],
                         index=['Vessel_1', 'Vessel_2', 'Vessel_3', 'Vessel_4', 'Vessel_5'])

print("Current pressures:")
print(current_pressures)
print("\nMaximum allowed pressures:")
print(max_pressures)

# Find vessels exceeding limits
alarm_conditions = current_pressures > max_pressures
vessels_in_alarm = current_pressures[alarm_conditions]

print("\nVessels in alarm:")
print(vessels_in_alarm)
print()

# ============================================================================
# PART 9: SERIES METHODS COMMONLY USED IN ENGINEERING
# ============================================================================

print("9. Common Series methods for engineering analysis")
print("-" * 50)

# Create sample process data
process_values = pd.Series([98.2, 99.1, 98.7, 102.3, 97.8, 98.9, 99.5, 98.1, 99.8, 98.4])

print("Sample process values:")
print(process_values)
print()

# Descriptive statistics
print("Descriptive statistics:")
print(f"Count: {process_values.count()}")
print(f"Mean: {process_values.mean():.2f}")
print(f"Median: {process_values.median():.2f}")
print(f"Std: {process_values.std():.2f}")
print(f"Min: {process_values.min():.2f}")
print(f"Max: {process_values.max():.2f}")
print()

# Finding extreme values
print("Finding extreme values:")
print(f"Index of maximum value: {process_values.idxmax()}")
print(f"Index of minimum value: {process_values.idxmin()}")
print()

# Sorting
print("Sorted values (ascending):")
print(process_values.sort_values())
print()

# Value counts (useful for categorical data)
equipment_status = pd.Series(['Running', 'Stopped', 'Running', 'Maintenance', 'Running', 'Stopped'])
print("Equipment status counts:")
print(equipment_status.value_counts())
print()

# ============================================================================
# PART 10: KEY TAKEAWAYS
# ============================================================================

print("=== KEY TAKEAWAYS ===")
print()

print("Understanding Series is crucial because:")
print("1. DataFrames are collections of Series with aligned indices")
print("2. Many DataFrame operations return Series")
print("3. Series operations are the foundation of data analysis")
print("4. Index alignment makes pandas powerful for engineering data")
print()

print("Series vs DataFrame:")
print("- Series: 1-dimensional, like a single sensor over time")
print("- DataFrame: 2-dimensional, like multiple sensors over time")
print("- Both share the same index-based alignment behavior")
print()

print("Common engineering use cases for Series:")
print("- Time series data from a single sensor")
print("- Equipment parameters (temperature, pressure, flow)")
print("- Calibration factors and correction values")
print("- Alarm thresholds and setpoints")
print("- Efficiency calculations and performance metrics")
print()

print("Next steps:")
print("- Practice creating Series with different index types")
print("- Experiment with mathematical operations on Series")
print("- Try combining multiple Series into DataFrames")
print("- Explore time-based indexing for process data")