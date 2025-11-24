# -*- coding: utf-8 -*-
"""
7.7 Skapa en DataFrame med saknade värden (NaN):

    import numpy as np

    df = pd.DataFrame({
        'A': [1, 2, np.nan, 4, 5],
        'B': [10, np.nan, 30, np.nan, 50],
        'C': [100, 200, 300, 400, 500]
    })

    a)    Hitta alla rader med saknade värden
    b)    Fyll saknade värden med medelvärdet av kolumnen
    c)    Ta bort alla rader med saknade värden
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [10, np.nan, 30, np.nan, 50],
    'C': [100, 200, 300, 400, 500]
})

print("DataFrame med saknade värden:")
print(df)
print()

# a) Hitta alla rader med saknade värden

print("Rader med saknade värden:")
missing_values = df[df.isnull().any(axis=1)]
print(missing_values)
print()

# b) Fyll saknade värden med medelvärdet av kolumnen

df_filled = df.fillna(df.mean())
print("DataFrame efter att ha fyllt saknade värden med medelvärdet:")
print(df_filled)
print()

# c) Ta bort alla rader med saknade värden

df_dropped = df.dropna()
print("DataFrame efter att ha tagit bort rader med saknade värden:")
print(df_dropped)
print()

