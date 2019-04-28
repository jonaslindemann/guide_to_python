# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:19:00 2017

@author: Jonas Lindemann
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 2*np.pi, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)


plt.figure(1)
plt.plot(x, y1, 'r-')

plt.figure(2)
plt.plot(x, y2, 'b-')

plt.show()