# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 17:37:06 2019

@author: Jonas Lindemann
"""

import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])

b = a.reshape([12,])
c = np.reshape(b, [12,])

print(b)
print(c)
