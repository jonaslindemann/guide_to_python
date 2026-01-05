# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import time

seconds = time.time()

import time, random, math

print('Start timing')

t0 = time.process_time()
for i in range(1000000):
    y = math.sin(random.random())
t1 = time.process_time()

print('End timing')

print('Elapsed time (s) = ', (t1-t0) + (t1-t0))
