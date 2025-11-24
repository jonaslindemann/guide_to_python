# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import os

os.system('notepad.exe')
print('Detta skrivs ut när processen avslutats!')

return_value = os.system('dir')
print("Programmet returnerade", return_value)
