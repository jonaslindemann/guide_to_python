# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:56:56 2019

@author: Jonas Lindemann
"""

a = [3, 6, 8, 10, 34, 32]
b = [76, 45, 10, 6, 89, 11]
c = []

for v1, v2 in zip(a, b):
    c.append(v1+v2)
    
print(c)
