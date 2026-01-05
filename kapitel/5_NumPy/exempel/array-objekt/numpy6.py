# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 00:47:49 2018

@author: Jonas Lindemann
"""

import numpy as np

b = np.array([[1,2],[3,4]])
print("array shape    =", b.shape)    # Storlek
print("array ndim     =", b.ndim)     # Antal dimensioner
print("array dtype    =", b.dtype)    # Datatyp
print("array size     =", b.size)     # Totalt antal element 
print("array itemsize =", b.itemsize) # storlek på datatype i byte
