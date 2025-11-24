# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 19:19:35 2019

@author: Jonas Lindemann
"""

list_of_strings = ["Detta", "är", "en", "lista", "med", "ord"]
list_of_things = ["tree", "house", "pencil", "eraser"]

s1 = " ".join(list_of_strings)
s2 = ",".join(list_of_things)
s3 = "".join(list_of_things)

print(s1)
print(s2)
print(s3)