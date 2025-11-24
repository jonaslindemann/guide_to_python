# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 00:47:49 2018

@author: Jonas Lindemann
"""

import numpy as np

def memory_of(a):
    return a.__array_interface__["data"][0]

a = np.array([[1,2],[3,4]])
print(a)
print(memory_of(a))

a_flat = np.reshape(a, [4,1])
print(a_flat)
print(memory_of(a_flat))

a[0,0] = 42
print(a)
print(a_flat)

c = a.copy()
c[0,0] = 84
print(a)
print(memory_of(a))
print(c)
print(memory_of(c))

b = a.reshape((4,))
print(b)
print(memory_of(b))