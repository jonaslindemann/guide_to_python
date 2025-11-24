# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 23:13:46 2019

@author: Jonas Lindemann
"""

import pathlib as pl

p = pl.Path(".")

for x in p.iterdir():
    if x.is_dir():
        print(x,'- katalog')
    else:
        print(x,'- fil')
