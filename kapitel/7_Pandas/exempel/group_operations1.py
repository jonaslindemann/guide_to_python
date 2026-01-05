import pandas as pd

# Läs in sensor­data
df = pd.read_csv('sensor_readings.csv', parse_dates=['timestamp'])

# Gruppera per sensor och beräkna medelvärde av temperatur och tryck
grouped = (
    df
    .groupby('sensor_id')[['temperature_C','pressure_bar']]
    .agg(['mean','min','max'])
    .reset_index()
)

print(grouped)