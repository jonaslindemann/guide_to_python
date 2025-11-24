# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.0, 1.0, 100).reshape([100, 1])
y = (0.5 + np.linspace(0.0, 1.0, 100) + np.random.uniform(-0.1, 0.1, 100)).reshape([100, 1])

X = np.asmatrix(np.ones([100, 2]))
Y = np.asmatrix(np.zeros([100, 1]))

X[:, 1] = x[:]
Y[:, 0] = y[:]

b = (X.T*X).I*X.T*Y

print(b)

x0 = 0.0
y0 = b[0, 0] + b[1, 0]*x0
x1 = 1.0
y1 = b[0, 0] + b[1, 0]*x1

plt.plot(x, y, 'o', [x0, x1], [y0, y1], 'r-')
plt.show()

