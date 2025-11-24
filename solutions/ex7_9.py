# -*- coding: utf-8 -*-
"""
7.9 Skapa en DataFrame med väderdata:

a)    Spara den som CSV-fil
b)    Läs in CSV-filen igen
c)    Spara som Excel-fil med två olika sheets
"""

import pandas as pd

weather = pd.DataFrame({
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Temperature': [22, 21, 23, 20, 19],
    'Humidity': [30, 45, 50, 40, 35]
})

# a) Spara den som CSV-fil

weather.to_csv('weather_data.csv', index=False)
print("Weather data sparad som weather_data.csv")

# b) Läs in CSV-filen igen

loaded_weather = pd.read_csv('weather_data.csv')
print("Inläst weather data från CSV:")
print(loaded_weather)

# c) Spara som Excel-fil med två olika sheets

with pd.ExcelWriter('weather_data.xlsx') as writer:
    weather.to_excel(writer, sheet_name='Sheet1', index=False)
    weather.to_excel(writer, sheet_name='Sheet2', index=False)  

print("Weather data sparad som weather_data.xlsx med två sheets")