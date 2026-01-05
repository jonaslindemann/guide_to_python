# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 16:06:38 2018

@author: Jonas Lindemann
"""

import numpy as np

a = np.array([[1,2],[3,4]], float)
print(a)
print(a.data)
print(a.shape)

b = np.reshape(a, [4,1])
print(b)
print(b.data)
print(b.shape)

