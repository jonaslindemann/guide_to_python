# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 14:58:33 2019

@author: Jonas Lindemann
"""

sum = 0.0
n = 1
diff = 1e6

while diff>1e-6:
    last_sum = sum
    sum += 1/(pow(3,n))
    diff = sum - last_sum

    n += 1

    print("Iteration", n, "sum = ", sum, "diff = ", diff)
