# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import os, time, random, math

print('Start timing')

t0 = os.times()
for i in range(1000000):
    y = math.sin(random.random())
t1 = os.times()

print('End timing')

print('Elapsed time (user+system) = ', (t1.user-t0.user) + (t1.system-t0.system))
