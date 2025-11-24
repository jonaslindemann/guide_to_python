# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import os

with os.scandir() as it:
    for entry in it:
        print("------------------------")
        print("name", entry.name)
        print("path", entry.path)
        print("is_dir", entry.is_dir())
        print("is_file", entry.is_file())
