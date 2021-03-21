# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 17:15:51 2019

@author: Jonas Lindemann
"""

# https://github.com/jonaslindemann/guide_to_python/blob/master/exercises/resources/secret.zip

import urllib.request
import zipfile as zf

with urllib.request.urlopen("https://github.com/jonaslindemann/guide_to_python/raw/master/exercises/resources/secret.zip") as response:
   data = response.read()

with open("secret.zip", "wb") as image_file:
    image_file.write(data)
    
with zf.ZipFile("secret.zip", "r") as myzip:
    print(myzip.namelist())
    myzip.extractall()
