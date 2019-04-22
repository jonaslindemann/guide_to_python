# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 16:48:41 2019

@author: Jonas Lindemann
"""

s = "Far far away, behind the word mountains, far from the countries " \
    "Vokalia and Consonantia, there live the blind texts. Separated they " \
    "live in Bookmarksgrove right at the coast of the Semantics, a large " \
    "language ocean."
    
if "Vokalia" in s:
    print("Hittade Vokalia i strängen")


pos = s.find("far")
print(pos)

pos = s.find("far", pos+1)
print(pos)

pos = s.find("python")
print(pos)


