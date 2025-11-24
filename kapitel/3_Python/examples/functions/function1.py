# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 09:44:16 2019

@author: Jonas Lindemann
"""

def f(x):
    return x**3 - x - 1

def f_p(x):
    return 3*(x**2) - 1

def newton_raphson(x0, f, f_p, eps=1e-6):

    diff = 1e300
   
    while diff > eps:
        x1 = x0 - f(x0)/f_p(x0)
        diff = abs(x1 - x0)
        x0 = x1
        
    return x0
        
if __name__ == "__main__":
    
    x = newton_raphson(1.0, f, f_p)
    
    print(x)