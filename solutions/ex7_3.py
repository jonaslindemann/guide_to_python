# -*- coding: utf-8 -*-
"""
7.3 Givet följande DataFrame:

    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [100, 200, 300, 400, 500]
    })

Välj:

    a)    Kolumn ’B’
    b)    Rad 2 med .iloc[]
    c)    Rader 1-3 med .loc[]
    d)    Alla rader där kolumn ’A’ > 2
"""

import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
})

print("DataFrame:")
print(df)
print()

# a) Kolumn 'B'

print("Kolumn 'B':")
print(df['B'])
print()

# b) Rad 2 med .iloc[]

print("Rad 2 med .iloc[]:")
print(df.iloc[2])
print()

# c) Rader 1-3 med .loc[]
print("Rader 1-3 med .loc[]:")
print(df.loc[1:3])
print()

