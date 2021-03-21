# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 17:55:58 2019

@author: Jonas Lindemann
"""

import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
a.resize([12,12])

b = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
c = np.resize(b, [12,12])

print(a)
print(c)
