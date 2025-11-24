#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 11:19:14 2018

@author: lindemann
"""

try:
    with open("myfil.txt", "r") as text_file:
        lines = text_file.readlines()
except:
    print("Filen kunde inte öppnas")





