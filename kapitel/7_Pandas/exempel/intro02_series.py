import pandas as pd
import numpy as np

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
