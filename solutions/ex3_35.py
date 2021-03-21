# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 17:07:36 2019

@author: Jonas Lindemann
"""

from math import *

def f(x):
    return sin(x)

def func_table(a, b, dx, f):

    print("{x_label:^10}{y_label:^10}".format(x_label="x", y_label="f(x)"))
    
    x = a    
    while x<=b:
        print("{x:<10.4f} {f:<10.4f}".format(x = x, f = f(x)))
        x += dx
        
if __name__ == "__main__":
    
    func_table(-2*pi, 2*pi, 0.1, f)
    
    