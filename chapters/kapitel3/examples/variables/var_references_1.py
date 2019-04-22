# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 17:50:49 2019

@author: Jonas Lindemann
"""

a = 42
b = 84

print(a, id(a))
print(b, id(b))

a = b

print("a = b")
print(a, id(a))
print(b, id(b))

a = 21

print("a = 21")
print(a, id(a))
print(b, id(b))
