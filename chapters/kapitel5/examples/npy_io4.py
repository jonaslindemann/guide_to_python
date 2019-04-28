# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import numpy as np
import matplotlib.pyplot as plt

with open("xy.dat", "rb") as f:
    x = np.load(f)
    y = np.load(f)

plt.plot(x, y, 'o')
plt.show()
