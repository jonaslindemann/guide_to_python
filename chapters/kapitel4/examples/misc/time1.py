# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import time

seconds = time.time()
print(seconds)

t_gm = time.gmtime(seconds)
t_local = time.localtime(seconds)

print(t_gm)
print(t_local)
print(time.asctime(t_gm))
print(time.asctime(t_local))
print(time.asctime())

sec_gm = time.mktime(t_gm)
sec_local = time.mktime(t_local)

print(sec_gm)
print(sec_local)

