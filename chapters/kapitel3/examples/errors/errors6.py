#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 13:59:50 2018

@author: lindemann
"""

try:
    with open("myfil.txt", "r") as text_file:
        lines = text_file.readlines()
except FileNotFoundError as e:
    print("Filen", e.filename, "kunde inte öppas.")
except PermissionError as e:
    print("Felsträngen är '"+e.strerror+"'")