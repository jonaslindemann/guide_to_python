# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import numpy as np

a = np.arange(10)
a = a * 10  # This will make a copy of a
print(a)

# Again with a ufunc.

a = np.arange(10)
np.multiply(a, 10, a)
print(a)
