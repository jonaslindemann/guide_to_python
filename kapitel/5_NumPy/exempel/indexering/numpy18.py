# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import numpy as np

def memory_of(a):
    return a.__array_interface__["data"][0]

a = np.arange(25)
print(a)
print(memory_of(a))
print(a.data)

b = a[1:5]
print(b)
print(memory_of(b))
print(b.data)

b[0] = 42
print(a)
print(b)