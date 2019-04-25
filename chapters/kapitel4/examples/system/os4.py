# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import os

for item in os.listdir():
    print(item)

for item in os.listdir():
    if os.path.isdir(item):
        print("Katalog:", item)
    if os.path.isfile(item):
        print("Fil    :", item)