# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import json

my_data = {"a number": 42, "a list": [1, 2, 3, 4], "a dict": {'a': 1, 'b': 2}}

json_string = json.dumps(my_data)

print(json_string)

my_data_copy = json.loads(json_string)

print(my_data_copy)