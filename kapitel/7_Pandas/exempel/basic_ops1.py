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