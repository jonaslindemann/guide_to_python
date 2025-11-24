# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:19:00 2017

@author: Jonas Lindemann
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# example data
x1 = np.arange(20)*2
x2 = np.arange(20)*2+1
y1 = np.random.rand(20)
y2 = np.random.rand(20)

plt.bar(x1, y1)
plt.bar(x2, y2)
plt.title("Stapeldiagram")
plt.xticks([])
plt.xlabel('x')
plt.ylabel('y')

plt.show()