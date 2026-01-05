import pandas as pd
import numpy as np

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
