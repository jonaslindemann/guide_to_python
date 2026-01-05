#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 11:19:14 2018

@author: lindemann
"""

text_file = open("myfile.txt", "w")
text_file.write("Filens innehåll. ")
text_file.write("Detta skrivs ut på samma rad.\n")
text_file.write("Denna text kommer på en ny rad")
text_file.close()