# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import numpy as np

a = np.arange(25)
print(a)
print(a[2])

b = np.arange(25).reshape([5,5])
print(b)
print(b[1,2])

a[2] = 42
b[1,2] = 42

print(a)
print(b)