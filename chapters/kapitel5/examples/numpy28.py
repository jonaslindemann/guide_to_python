# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import numpy as np

A = np.matrix([[1, 2, 3], [11, 12, 13], [21, 22, 23]])
x = np.matrix([[1], [2], [3]])

print(A)
print(x)

b = np.linalg.solve(A, x)

print(b)