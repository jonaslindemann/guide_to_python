# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:19:00 2017

@author: Jonas Lindemann
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,2.0, 0.01)
y1 = x
y2 = np.exp(x)

plt.figure(1)
plt.title("Logaritmisk skalning av y")
plt.yscale('log')
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y1, 'r-', x, y2, 'b-')

plt.figure(2)
plt.title("Linjär skalning av y")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y1, 'r-', x, y2, 'b-')

plt.show()