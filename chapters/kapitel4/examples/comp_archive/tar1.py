# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import tarfile as tf

with tf.TarFile("myarchive.tar.gz", "w") as mytar:
    mytar.add("tempfile1.py")
    mytar.add("tempfile2.py")

with tf.TarFile("myarchive.tar.gz", "r") as mytar:
    print(mytar.getnames())
    print(mytar.getmembers())
    mytar.extract("tempfile1.py", "mytar")
    mytar.extractall("mytar_all")
    mytar.list(verbose=True)

