# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 19:53:16 2019

@author: Jonas Lindemann
"""

import numpy as np

a = np.arange(36).reshape(6,6)
print(a)

# a) värdet på rad 2, kolumn 2

print(a[1,1])

# b) rad 3

print(a[2])
print(a[2,:])

# c) kolumn 4

print(a[:,3])

# d) sista raden

print(a[-1])

# e) sista kolumnen

print(a[:,-1])

# f) näst sista raden

print(a[-2])
