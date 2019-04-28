# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import numpy as np

a = np.arange(10)
print(a)

b = np.reshape(np.arange(100), [10,10])
print(b)

a = np.arange(0,10)
print(a)

a = np.arange(-10,10)
print(a)

a = np.arange(-10,10,2)
print(a)

a = np.arange(-10,10,2, dtype=float)
print(a)
