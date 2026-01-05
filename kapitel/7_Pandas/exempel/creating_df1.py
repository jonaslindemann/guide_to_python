import pandas as pd
import numpy as np

# Engineering sensor data
sensor_data = {
    'timestamp': pd.date_range('2024-01-01', periods=100, freq='1H'),
    'temperature_c': np.random.normal(25, 5, 100),
    'pressure_bar': np.random.normal(1.013, 0.1, 100),
    'flow_rate_lpm': np.random.normal(50, 10, 100),
    'sensor_id': ['T001', 'P001', 'F001'] * 33 + ['T001']
}

df = pd.DataFrame(sensor_data)
print("Engineering Data Overview:")
print(df.head())
print(f"\nDataFrame shape: {df.shape}")
print(f"Data types:\n{df.dtypes}")

# Quick statistics for engineering analysis
print("Temperature Statistics:")
print(df['temperature_c'].describe())

# Check for out-of-range values (engineering limits)
temp_alerts = df[df['temperature_c'] > 35]  # Temperature alert threshold
pressure_alerts = df[df['pressure_bar'] < 0.9]  # Low pressure alert

print(f"\nTemperature alerts: {len(temp_alerts)} readings")
print(f"Pressure alerts: {len(pressure_alerts)} readings")

# Calculate derived engineering metrics
df['temp_deviation'] = df['temperature_c'] - df['temperature_c'].mean()
df['pressure_psi'] = df['pressure_bar'] * 14.5038  # Convert bar to psi