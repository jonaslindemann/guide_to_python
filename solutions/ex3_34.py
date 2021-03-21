# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 17:07:36 2019

@author: Jonas Lindemann
"""

def f(x):
    return x**3 - x - 1

def deriv_f(f, x, h=1e-6):
    return (f(x + h) - f(x))/h
       
if __name__ == "__main__":
    
    print("fprim(1.0) =", deriv_f(f, 1.0))
