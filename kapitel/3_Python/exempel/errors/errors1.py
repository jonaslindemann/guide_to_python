#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 11:19:14 2018

@author: lindemann
"""

import os

filename = "myfil.txt"

if os.path.exists(filename):
    with open("myfil.txt", "r") as text_file:
        lines = text_file.readlines()
else:
    print("Filen "+filename+" hittades inte!")

