# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 14:35:46 2019

@author: Jonas Lindemann
"""

values = [1, 3, 6, 4, 'hej', 1.0] # Tilldelning av lista med  värden

# Delområde från från 1 >= idx < 3

print(values[1:3])

# Delområde från från 1 >= idx < len(values)-2

print(values[1:-1])

# Delområde från idx >= 3

print(values[3:])

# Alla element i listan

print(values[:])

# Delområde från från 0 >= idx < len(values)-2

print(values[:-2])

# Delområde från len(values)-3 >= idx < len(values)-1

print(values[-3:])

