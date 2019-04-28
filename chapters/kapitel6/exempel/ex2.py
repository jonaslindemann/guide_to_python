# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:15:13 2017

@author: Jonas Lindemann
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 2*np.pi, 1000)
y = np.sin(x)

plt.plot(x, y)
plt.show()