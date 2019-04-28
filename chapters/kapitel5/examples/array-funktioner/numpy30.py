# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 20:33:03 2019

@author: Jonas Lindemann
"""

import numpy as np

a = np.arange(36).reshape(6,6)
print(a)

print(a.sum())

print(a.sum(0))
print(a.sum(1))