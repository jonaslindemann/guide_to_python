# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 00:00:09 2019

@author: Jonas Lindemann
"""

import os
import pathlib as pl

new_path = pl.Path('..')
old_path = pl.Path.cwd()

os.chdir(new_path)

print(pl.Path.cwd())

os.chdir(old_path)

print(pl.Path.cwd())
