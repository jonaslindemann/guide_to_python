# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import json

my_data = {"a number": 42, "a list": [1, 2, 3, 4], "a dict": {'a': 1, 'b': 2}}

with open("mydata.json", "w") as my_file:
    json.dump(my_data, my_file)

with open("mydata.json", "r") as my_file:
    my_data_copy = json.load(my_file)

print(my_data_copy)