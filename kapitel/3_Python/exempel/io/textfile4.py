#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 11:19:14 2018

@author: lindemann
"""

text_file = open("myfile.txt", "r")

line = text_file.readline().rstrip()
while line!='':
    print(">"+line)
    line = text_file.readline().rstrip()

text_file.close()