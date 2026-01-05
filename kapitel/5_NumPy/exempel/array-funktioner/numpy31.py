# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 21:53:30 2019

@author: Jonas Lindemann
"""

import numpy as np

a = np.arange(1,37,dtype=float).reshape(6,6)
print(a)

print(a.prod())
print(a.prod(0)) # Produkten av kolumner
print(a.prod(1)) # Produkten av rader