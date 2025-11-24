# -*- coding: utf-8 -*-
"""
7.10 Skapa en DataFrame med datumsindex för en månad:

    dates = pd.date_range('2024-01-01', periods=30, freq='D')
    df = pd.DataFrame({'Temperatur': np.random.randint(-5, 15, 30)},
                    index=dates)

    a)    Välj alla mätningar från vecka 2
    b)    Beräkna rullande medelvärde (7 dagar)
    c)    Gruppera per vecka och beräkna medeltemperatur
"""

import pandas as pd
import numpy as np

dates = pd.date_range('2024-01-01', periods=30, freq='D')
df = pd.DataFrame({'Temperatur': np.random.randint(-5, 15, 30)},
                  index=dates)

print("DataFrame med datumsindex:")
print(df)
print()

# a) Välj alla mätningar från vecka 2

print("Mätningar från vecka 2:")
week_2 = df['2024-01-08':'2024-01-14']
print(week_2)
print()

# b) Beräkna rullande medelvärde (7 dagar)

print("Rullande medelvärde (7 dagar):")
rolling_mean = df.rolling(window=7).mean()
print(rolling_mean)
print()

# c) Gruppera per vecka och beräkna medeltemperatur

print("Medeltemperatur per vecka:")
weekly_mean = df.resample('W').mean()
print(weekly_mean)
print()


