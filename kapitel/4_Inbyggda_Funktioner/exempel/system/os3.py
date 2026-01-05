# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import os

cwd = os.getcwd()
print(cwd)

os.chdir("..")
print(os.getcwd())
os.chdir(cwd)

