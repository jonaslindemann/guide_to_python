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

s1 = 200.0 * np.random.rand(n)
s2 = 200.0 * np.random.rand(n)
s3 = 200.0 * np.random.rand(n)

plt.scatter(x1, y1, c='red', s=s1, label='Serie 1', alpha=0.3, edgecolors='none')
plt.scatter(x2, y2, c='green', s=s2, label='Serie 2', alpha=0.3, edgecolors='none')
plt.scatter(x3, y3, c='blue', s=s3, label='Serie 3', alpha=0.3, edgecolors='none')

plt.title('Plottning av punkter')
plt.legend()
plt.grid(True)

plt.show()