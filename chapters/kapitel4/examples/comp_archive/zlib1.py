# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import pickle, zlib

my_data = {"a number": 42, "a list": list(range(1000)), "a dict": {'a': 1, 'b': 2}}

my_data_dump = pickle.dumps(my_data)
print(len(my_data_dump))

my_data_compressed = zlib.compress(my_data_dump)
print(len(my_data_compressed))

my_data_uncompressed = zlib.decompress(my_data_compressed)

my_data_copy = pickle.loads(my_data_uncompressed)
print(my_data_copy)

