# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 13:52:04 2017

@author: Jonas Lindemann
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

N = 100
M = 100

x = np.linspace(-3.0, 3.0, M)
y = np.linspace(-3.0, 3.0, N)

X, Y = np.meshgrid(x, y)

Z = np.sin(0.5*X*Y)

fig1 = plt.figure(1)
axes1 = fig1.add_subplot(111, projection='3d')

plt.title(r"Konturplott $sin(x=\frac{pi}{2})$")
axes1.contour(X, Y, Z, 6)

fig2 = plt.figure(2)
axes2 = fig2.add_subplot(111, projection='3d')

plt.title(r"Konturplott $sin(x=\frac{pi}{2})$")
axes2.contourf(X, Y, Z, 6)

plt.show()

