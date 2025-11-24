# -*- coding: utf-8 -*-
"""
7.12 Projekt - Temperaturanalys:

Skapa en DataFrame med simulerad temperaturdata för 3 städer över ett år (365 dagar). Utför följande:

a)    Beräkna månadsmedelvärden per stad
b)    Hitta varmaste och kallaste dagen per stad
c)    Jämför städernas temperaturvariationer
d)    Exportera resultaten till Excel med separata sheets per stad
"""

import pandas as pd
import numpy as np

# Skapa datumsindex för ett år

dates = pd.date_range('2024-01-01', periods=365, freq='D')

# Simulera temperaturdata för 3 städer

np.random.seed(0)  # För reproducerbarhet

data = {
    'CityA': np.random.randint(-10, 30, size=365),
    'CityB': np.random.randint(-5, 35, size=365),
    'CityC': np.random.randint(0, 40, size=365)
}

df = pd.DataFrame(data, index=dates)
print("Temperaturdata för 3 städer över ett år:")
print(df)
print()

# a) Beräkna månadsmedelvärden per stad

monthly_means = df.resample('M').mean()
print("Månadsmedelvärden per stad:")
print(monthly_means)

# b) Hitta varmaste och kallaste dagen per stad

hottest_days = df.idxmax()
coldest_days = df.idxmin()

coldest_temp = df.min()
hottest_temp = df.max()

# Create DataFrames with date and corresponding hottest and coldest values

hottest_df = pd.DataFrame({
    'City': df.columns,
    'Hottest Date': hottest_days.values,
    'Temperature': hottest_temp.values
})

coldest_df = pd.DataFrame({
    'City': df.columns,
    'Coldest Date': coldest_days.values,
    'Temperature': coldest_temp.values
})

print("\nVarmaste dagen per stad:")
print(hottest_df)
print("\nKallaste dagen per stad:")
print(coldest_df)

# c) Jämför städernas temperaturvariationer

variations = df.std()

print("\nTemperaturvariationer per stad (standardavvikelse):")
print(variations)

# d) Exportera resultaten till Excel med separata sheets per stad

with pd.ExcelWriter('temperature_analysis.xlsx') as writer:
    for city in df.columns:
        city_data = df[[city]]
        city_data.to_excel(writer, sheet_name=city)
    monthly_means.to_excel(writer, sheet_name='Monthly Means')
    variations.to_frame(name='Std Dev').to_excel(writer, sheet_name='Variations')  