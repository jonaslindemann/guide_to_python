# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 13:47:15 2019

@author: Jonas Lindemann
"""

l = [
     [45, 78, 56, 34],
     [9, 23, 23],
     [34, 87],
     [12, 19, 78, 56, 45]
]

with open("ex1_36.txt", "w") as text_file:
    for row in l:
        for value in row:
            text_file.write(str(value)+" ")
        text_file.write("\n")
        
    