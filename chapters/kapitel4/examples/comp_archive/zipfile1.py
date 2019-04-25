# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import zipfile as zf

with zf.ZipFile("myarchive.zip", "w") as myzip:
    myzip.write("tempfile1.py")
    myzip.write("tempfile2.py")

with zf.ZipFile("myarchive.zip", "r") as myzip:
    print(myzip.namelist())
    print(myzip.getinfo("tempfile1.py"))
    myzip.extract("tempfile2.py", "myzip")
    myzip.extractall("myzip_all")
    myzip.printdir()
    with myzip.open("tempfile1.py") as myfile:
        print(myfile.read())

