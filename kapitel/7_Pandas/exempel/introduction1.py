
import numpy as np
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])

print(s)

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

print(s)

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], name='numbers')

print(s)

d = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }

s = pd.Series(d)

print(s)

random_values = np.random.normal(50, 10, 26)

s = pd.Series(random_values, index=list('abcdefghijklmnopqrstuvwxyz'))

print(s)
print(s.iloc[0])
print(s.iloc[:3])
print(s.iloc[1:4])
print(s[0])
print(s[s>s.mean()])
print('a' in s)   
print('1' in s)   
arr = s.to_numpy()

