# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import numpy as np

a = np.arange(25).reshape([5,5])
print(a)

print(a+3) # Elementvis addition
print(a*3) # Elementvis multiplikation
print(np.sin(a))
print(-a)
print(a+a)

a = np.array([1,2,3])
b = np.ones([5,3])
print(a)
print(b)

print(a+b)
