# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import pickle

my_data = {"a number": 42, "a list": [1, 2, 3, 4], "a dict": {'a': 1, 'b': 2}}

my_data_dump = pickle.dumps(my_data)

print(my_data_dump)

my_data_copy = pickle.loads(my_data_dump)

print(my_data_copy)

