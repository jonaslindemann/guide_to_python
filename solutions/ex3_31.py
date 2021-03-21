# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 15:10:05 2019

@author: Jonas Lindemann
"""

from math import sqrt

for n in range(2,100):
    
    prime = True
    
    k = 2
    while k<=sqrt(n) and prime:
        if (n % k == 0):
            prime = False
            break
        k+=1      
        
    if prime:
        print("n =", n, "är ett primtal.")
        

            
