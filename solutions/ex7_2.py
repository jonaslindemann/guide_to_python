# -*- coding: utf-8 -*-
"""
6.2 Givet följande DataFrame:


df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
})

Visa:

a)    shape, columns, dtypes och index
b)    De tre första raderna
c)    Statistisk sammanfattning med describe()

"""

import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
})

# a) shape, columns, dtypes och index

print("Shape:")
print(df.shape)
print()
print("Columns:")
print(df.columns)
print()
print("Dtypes:")
print(df.dtypes)
print()
print("Index:")
print(df.index)
print()

# b) De tre första raderna

print("De tre första raderna:")
print(df.head(3))
print()

# c) Statistisk sammanfattning med describe()

print("Statistisk sammanfattning med describe():")
print(df.describe())
print()

