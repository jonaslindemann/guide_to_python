# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 19:53:16 2019

@author: Jonas Lindemann
"""

import numpy as np

A = np.random.randint(0, 100, [5, 5])
B = np.random.randint(0, 100, [5, 5])

C = A @ B

print(C)