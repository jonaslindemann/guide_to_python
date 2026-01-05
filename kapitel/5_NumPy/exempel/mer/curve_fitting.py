# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.0, 1.0, 10)
y = np.random.uniform(0.0, 1.0, 10)

p = np.polyfit(x, y, 6)
print(p)

xp = np.linspace(0.0, 1.0, 1000)
yp = np.polyval(p, xp)

print(r)

plt.plot(x, y, 'o', xp, yp, 'r-')
plt.show()

