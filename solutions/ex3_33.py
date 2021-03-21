# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 15:48:35 2019

@author: Jonas Lindemann
"""

from random import randint

def zero_lt_zero(l):
    for i in range(len(l)):
        if l[i]<0:
            l[i] = 0
            
l = [randint(-100,101) for i in range(100)]

zero_lt_zero(l)

print(l)

