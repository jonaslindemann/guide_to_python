# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import pickle

my_data = {"a number": 42, "a list": [1, 2, 3, 4], "a dict": {'a': 1, 'b': 2}}

with open("my_data_text.pkl", "wb") as my_file:
    pickle.dump(my_data, my_file, protocol=0)

with open("my_data_text.pkl", "rb") as my_file:
    my_data_copy = pickle.load(my_file)

print(my_data_copy)
