# -*- coding: utf-8 -*-
"""
7.11 Skapa en DataFrame med 100 studenters poäng i tre ämnen:

a)    Beräkna totalpoäng per student
b)    Hitta topp 10 studenter
c)    Skapa en ny kolumn ’Betyg’ baserat på totalpoäng (>85=’A’, >70=’B’, >55=’C’, annars=’F’)
d)    Räkna antal studenter per betyg
"""

import pandas as pd
import numpy as np

np.random.seed(0)  # För reproducerbarhet
data = {
    'StudentID': range(1, 101),
    'Math': np.random.randint(0, 101, size=100),
    'Science': np.random.randint(0, 101, size=100),
    'English': np.random.randint(0, 101, size=100)
}

df = pd.DataFrame(data)

print("DataFrame med studentpoäng:")
print(df)
print()

# a) Beräkna totalpoäng per student

df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
print("DataFrame med totalpoäng:")
print(df)
print()

# b) Hitta topp 10 studenter
print("Topp 10 studenter baserat på totalpoäng:")
top_10 = df.nlargest(10, 'Total')
print(top_10)
print()

# c) Skapa en ny kolumn 'Betyg' baserat på totalpoäng

def assign_grade(total):
    if total > 85:
        return 'A'
    elif total > 70:
        return 'B'
    elif total > 55:
        return 'C'
    else:
        return 'F'

df['Betyg'] = df['Total'].apply(assign_grade)
print("DataFrame med betyg:")
print(df)
print()

# d) Räkna antal studenter per betyg

grade_counts = df['Betyg'].value_counts()
print("Antal studenter per betyg:")
print(grade_counts)
print()

