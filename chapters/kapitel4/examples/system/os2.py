# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import os

exe_path_list = os.get_exec_path()

for path in exe_path_list:
    print(path)

