import pandas as pd
import numpy as np

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
print("---")

print(reactor_pressure.describe())  # Summary statistics