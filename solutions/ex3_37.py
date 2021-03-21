# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 13:57:32 2019

@author: Jonas Lindemann
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 13:47:15 2019

@author: Jonas Lindemann
"""

with open("ex1_36.txt", "r") as text_file:
    lines = text_file.readlines()
    
l = []

for line in lines:
    str_values = line.split()
    values = []
    
    for str_value in str_values:
        values.append(int(str_value))
        
    l.append(values)
    
print(l)
        
    