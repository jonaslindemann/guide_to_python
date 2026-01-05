# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import time

seconds = time.time()
print(seconds)

t_local = time.localtime(seconds)

time_format = '%a, %d %b %Y %H:%M:%S'

time_string = time.strftime(time_format, t_local)
print(time_string)

t_converted = time.strptime(time_string, time_format)
print(t_converted)