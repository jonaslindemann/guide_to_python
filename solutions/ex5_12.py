# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 19:53:16 2019

@author: Jonas Lindemann
"""

import numpy as np

a = np.arange(25).reshape([5,5])
print(a)

b = np.sin(a)*3 + 3.0

print(b)

