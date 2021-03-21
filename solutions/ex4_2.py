# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 19:41:54 2019

@author: Jonas Lindemann
"""

import os

if "PATH" in os.environ:
    print("PATH finns som miljövariabel.")
else:
    print("PATH fanns ej.")