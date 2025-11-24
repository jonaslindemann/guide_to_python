# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 13:52:04 2017

@author: Jonas Lindemann
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LightSource
import numpy as np

light = LightSource(90, 45)

N = 100
M = 100

x = np.linspace(-3.0, 3.0, M)
y = np.linspace(-3.0, 3.0, N)

X, Y = np.meshgrid(x, y)

Z = np.sin(0.5*X*Y)

fig = plt.figure()
axes = fig.add_subplot(111, projection='3d')

plt.title(r"Konturplott $sin(x=\frac{pi}{2})$")

axes.plot_surface(X, Y, Z, cmap=plt.cm.plasma)

plt.show()

