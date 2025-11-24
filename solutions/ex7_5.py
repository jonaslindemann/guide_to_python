# -*- coding: utf-8 -*-
"""
7.5 Givet en DataFrame med försäljningsdata:


sales = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Jan', 'Feb', 'Mar'],
    'Product': ['A', 'A', 'A', 'B', 'B', 'B'],
    'Sales': [100, 150, 120, 80, 90, 110]
})
a)    Lägg till en kolumn ’Quarter’ med värdet ’Q1’ för alla rader
b)    Beräkna en ny kolumn ’Tax’ som är 25% av ’Sales’
c)    Ta bort kolumnen ’Quarter’
"""

import pandas as pd
import numpy as np

sales = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Jan', 'Feb', 'Mar'],
    'Product': ['A', 'A', 'A', 'B', 'B', 'B'],
    'Sales': [100, 150, 120, 80, 90, 110]
})

print("Ursprunglig DataFrame:")
print(sales)
print()

# a) Lägg till en kolumn ’Quarter’ med värdet ’Q1’ för alla rader

sales['Quarter'] = 'Q1'
print("Efter att ha lagt till kolumnen 'Quarter':")
print(sales)
print()

# b) Beräkna en ny kolumn ’Tax’ som är 25% av ’Sales’

sales['Tax'] = sales['Sales'] * 0.25
print("Efter att ha lagt till kolumnen 'Tax':")
print(sales)
print()

# c) Ta bort kolumnen ’Quarter’

sales.drop(columns=['Quarter'], inplace=True)
print("Efter att ha tagit bort kolumnen 'Quarter':")
print(sales)
print()
