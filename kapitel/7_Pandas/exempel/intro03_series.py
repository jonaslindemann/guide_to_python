import pandas as pd
import numpy as np

equipment_temps = pd.Series(
    data=[78.5, 82.1, 76.3, 85.2, 79.8],
    index=['Pump_001', 'Motor_002', 'Tank_003', 'Compressor_004', 'Valve_005']
)

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