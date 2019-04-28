# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 13:52:04 2017

@author: Jonas Lindemann
"""

import matplotlib.pyplot as plt
import numpy as np

N = 5
M = 10

x = np.linspace(-3.0, 3.0, M)
y = np.linspace(-3.0, 3.0, N)

X, Y = np.meshgrid(x, y)

np.set_printoptions(precision=3)

print(X)
print(Y)