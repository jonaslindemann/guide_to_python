#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 11:19:14 2018

@author: lindemann
"""

with open("myfile.txt", "r") as text_file:
    lines = text_file.readlines()

print(lines)