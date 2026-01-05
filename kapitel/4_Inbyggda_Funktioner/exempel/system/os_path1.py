# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:05:32 2019

@author: Jonas Lindemann
"""

import os

current_dir = os.getcwd()

print(current_dir)

dir_name = "new_dir"

new_path = os.path.join(current_dir, dir_name)

print(new_path)