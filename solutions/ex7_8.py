# -*- coding: utf-8 -*-
"""
7.8 Skapa två DataFrames:

    df1 = pd.DataFrame({'ID': [1, 2, 3], 'Namn': ['Anna', 'Bertil', 'Cilla']})
    df2 = pd.DataFrame({'ID': [1, 2, 4], 'Lön': [30000, 35000, 40000]})

    a)    Gör en inner join på ’ID’
    b)    Gör en outer join
    c)    Slå ihop med concat() längs kolumnerna
"""

import pandas as pd

df1 = pd.DataFrame({'ID': [1, 2, 3], 'Namn': ['Anna', 'Bertil', 'Cilla']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Lön': [30000, 35000, 40000]})

print("DataFrame 1:")
print(df1)

print("DataFrame 2:")
print(df2)

# a) Gör en inner join på 'ID'

inner_join = pd.merge(df1, df2, on='ID', how='inner')
print("Inner join på 'ID':")
print(inner_join)
print()

# b) Gör en outer join

outer_join = pd.merge(df1, df2, on='ID', how='outer')
print("Outer join på 'ID':")
print(outer_join)
print()

# c) Slå ihop med concat() längs kolumnerna

concat_df = pd.concat([df1.set_index('ID'), df2.set_index('ID')], axis=1).reset_index()
print("Concat längs kolumnerna:")
print(concat_df)
print()
