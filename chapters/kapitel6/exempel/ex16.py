# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 13:47:33 2017

@author: Jonas Lindemann
"""

import matplotlib.pyplot as plt
import numpy as np

n = 200

x1, y1 = np.random.rand(2, n)
x2, y2 = np.random.rand(2, n)
x3, y3 = np.random.rand(2, n)

plt.scatter(x1, y1, c='red')
plt.scatter(x2, y2, c='green')
plt.scatter(x3, y3, c='blue')

plt.title('Plottning av punkter')
plt.legend()
plt.grid(True)

plt.show()