# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 14:40:06 2017

@author: Jonas Lindemann
"""

import numpy as np

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

N = 100

x = np.linspace(-3.0, 3.0, N)
y = np.linspace(-3.0, 3.0, N)

X, Y = np.meshgrid(x, y)

z = np.sin(0.5*X*Y)

#plt.ion()
fig = plt.figure()
ax = fig.gca(projection='3d')




ax.plot_surface(X, Y, z, cmap=plt.cm.RdBu)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_zlim(-5, 5)

plt.show()
#plt.draw()