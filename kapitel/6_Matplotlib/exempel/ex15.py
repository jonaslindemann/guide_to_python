# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:19:00 2017

@author: Jonas Lindemann
"""

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

np.random.seed(0)

# example data
x = np.arange(20)
y = np.random.rand(20)

plt.bar(x, y, tick_label=x)
plt.title("Stapeldiagram")
plt.xlabel('x')
plt.ylabel('y')

plt.show()