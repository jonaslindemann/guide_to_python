# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 13:52:04 2017

@author: Jonas Lindemann
"""

import matplotlib.pyplot as plt
import numpy as np

N = 100

x = np.linspace(-3.0, 3.0, N)
y = np.linspace(-3.0, 3.0, N)

X, Y = np.meshgrid(x, y)

# Funktionsyta

Z = np.sin(0.5*X*Y)

# Partiella derivator

dX = np.cos(0.5*X*Y)*0.5*Y
dY = np.cos(0.5*X*Y)*0.5*X

plt.title(r"Vektorplott $sin(x=\frac{pi}{2})$")
plt.contour(X, Y, Z, 6)

# Strömplott

plt.streamplot(X, Y, dX, dY, density=1)

plt.show()