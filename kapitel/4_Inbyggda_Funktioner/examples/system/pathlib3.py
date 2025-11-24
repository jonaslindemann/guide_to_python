# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 00:00:09 2019

@author: Jonas Lindemann
"""

import os
import pathlib as pl

p = pl.Path('..')

os.chdir(p)

q = pl.Path.cwd()
print(q)

