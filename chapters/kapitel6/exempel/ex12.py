# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:19:00 2017

@author: Jonas Lindemann
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.sin(x)


plt.figure(1)
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(0, np.pi)
plt.ylim(0, 1.5)
plt.annotate('max', xy=(np.pi/2, 1), xytext=(np.pi/2, 0.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center')
plt.plot(x, y, 'r-')

plt.show()