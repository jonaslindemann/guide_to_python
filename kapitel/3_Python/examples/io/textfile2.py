#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 11:19:14 2018

@author: lindemann
"""

text_file = open("myfile.txt", "r")
content = text_file.read()
text_file.close()

print(content)
