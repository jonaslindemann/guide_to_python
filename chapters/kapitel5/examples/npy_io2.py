# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.load("x.npy")
y = np.load("y.npy")

plt.plot(x, y, 'o')
plt.show()
