# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 23:50:26 2018

@author: Jonas Lindemann
"""

params = {"value1": 42, "value2": 3.14, "value3": "Python"}
print("{value1}, {value2}, {value3}".format(**params))
