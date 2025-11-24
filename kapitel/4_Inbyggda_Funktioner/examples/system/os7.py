# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import os

for root, dirs, files in os.walk("D:\\Users\\Jonas\\Development\\python_book\\book"):
    print("--->")
    print(root)
    print(dirs)
    print(files)
    print("<---")
