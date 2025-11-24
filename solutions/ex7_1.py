# -*- coding: utf-8 -*-
"""
7.1 Skapa följande Series och DataFrames:
a)    En Series med värdena [10, 20, 30, 40, 50] och index [’a’, ’b’, ’c’, ’d’, ’e’]
b)    En DataFrame med kolumner ’Namn’, ’Ålder’, ’Stad’ för 4 personer
c)    En DataFrame från en dictionary med tre kolumner och minst 5 rader
"""

import pandas as pd

# a) En Series med värdena [10, 20, 30, 40, 50] och index [’a’, ’b’, ’c’, ’d’, ’e’]

series_a = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print()
print("Series a):")
print()
print(series_a)
print()

# b) En DataFrame med kolumner ’Namn’, ’Ålder’, ’Stad’ för 4 personer

data_b = {
    'Namn': ['Alice', 'Bob', 'Charlie', 'David'],
    'Ålder': [25, 30, 35, 40],
    'Stad': ['Stockholm', 'Göteborg', 'Malmö', 'Uppsala']
}

df_b = pd.DataFrame(data_b)
print("DataFrame b):")
print()
print(df_b)
print()

# c) En DataFrame från en dictionary med tre kolumner och minst 5 rader

data_c = {
    'Kolumn1': [1, 2, 3, 4, 5],
    'Kolumn2': ['A', 'B', 'C', 'D', 'E'],
    'Kolumn3': [10.5, 20.5, 30.5, 40.5, 50.5]
}

df_c = pd.DataFrame(data_c)
print("DataFrame c):")
print()
print(df_c)
print()
