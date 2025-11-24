# -*- coding: utf-8 -*-
"""
7.6 Givet en DataFrame med försäljningsdata:

sales = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Jan', 'Feb', 'Mar'],
    'Product': ['A', 'A', 'A', 'B', 'B', 'B'],
    'Sales': [100, 150, 120, 80, 90, 110]
})

a)    Använd groupby() för att beräkna total försäljning per produkt
b)    Hitta medelvärde försäljning per månad
c)    Hitta max och min försäljning per produkt
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

# a) Använd groupby() för att beräkna total försäljning per produkt

total_sales_per_product = sales.groupby('Product')['Sales'].sum()
print("Total försäljning per produkt:")
print(total_sales_per_product)
print()

# b) Hitta medelvärde försäljning per månad

average_sales_per_month = sales.groupby('Month')['Sales'].mean()
print("Medelvärde försäljning per månad:")
print(average_sales_per_month)
print()

# c) Hitta max och min försäljning per produkt

max_min_sales_per_product = sales.groupby('Product')['Sales'].agg(['max', 'min'])
print("Max och min försäljning per produkt:")
print(max_min_sales_per_product)
print()
