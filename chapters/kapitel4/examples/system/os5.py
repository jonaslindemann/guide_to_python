# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import os

cwd = os.getcwd()

if not os.path.exists("os5"):
    os.mkdir("os5")

os.chdir("os5")

os.mkdir("testdir")

with open("testfile", "w") as f:
    f.write("testfile")

print(os.listdir())

os.rename("testfile", "testfile2")

print(os.listdir())

os.rmdir("testdir")
os.remove("testfile2")

print(os.listdir())

os.chdir(cwd)
