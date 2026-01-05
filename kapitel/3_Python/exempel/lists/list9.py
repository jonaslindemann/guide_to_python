# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:55:56 2019

@author: Jonas Lindemann
"""
b = [3, 4]
a = [1, 2, b.copy(), 5, 6]

b[0] = -1

print(b)
print(a)
