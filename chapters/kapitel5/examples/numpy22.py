# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import numpy as np

# add.reduce() används för att summera (reducere) ett
# array-objekt

a = np.arange(10)
print(a)
print(np.add.reduce(a))

# Snabbare än:

print(a.sum())