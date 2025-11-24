#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 13:59:50 2018

@author: lindemann
"""

try:
    input_file = open("numbers.txt", "r")
    output_file = open("sums.txt", "w")
    
    lines = input_file.readlines()
    for line in lines:
        items = line.strip().split()
        numbers = []
        for item in items:
            numbers.append(int(item))
            
        output_file.write("%d\n" % sum(numbers))
except ValueError:
    print("Felaktiga indata på rad", line)
finally:
    print("Stäng öppna filer.")
    input_file.close()
    output_file.close()
        
