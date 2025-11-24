# -*- coding: utf-8 -*-
"""
7.4 Skapa en DataFrame med 20 rader och kolumner: ’Produkt’, ’Pris’, ’Antal’:

a)    Filtrera produkter med pris > 50
b)    Hitta produkter där antal är mellan 10 och 50
c)    Sortera efter pris (fallande)   Alla rader där kolumn ’A’ > 2
"""

import pandas as pd
import numpy as np

prices = np.random.randint(10, 100, size=20)
quantities = np.random.randint(1, 100, size=20)
products = [f'Produkt{i}' for i in range(1, 21)]

df = pd.DataFrame({
    'Produkt': products,
    'Pris': prices,
    'Antal': quantities
})

print("DataFrame:")
print(df)
print()

# a) Filtrera produkter med pris > 50

print("Produkter med pris > 50:")
filtered_price = df[df['Pris'] > 50]
print(filtered_price)
print()

# b) Hitta produkter där antal är mellan 10 och 50

print("Produkter där antal är mellan 10 och 50:")
filtered_quantity = df[(df['Antal'] >= 10) & (df['Antal'] <= 50)]
print(filtered_quantity)
print()

# c) Sortera efter pris (fallande)

print("DataFrame sorterad efter pris (fallande):")
sorted_df = df.sort_values(by='Pris', ascending=False)
print(sorted_df)
print()

