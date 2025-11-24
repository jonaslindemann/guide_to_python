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

Z = np.sin(0.5*X*Y)

plt.title(r"Konturplott $sin(x=\frac{pi}{2})$")
plt.contour(X, Y, Z, 6)
plt.colorbar()

plt.show()