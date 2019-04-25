# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 15:27:36 2019

@author: Jonas Lindemann
"""

import urllib.request

with urllib.request.urlopen("https://bit.ly/2VOwNu1") as response:
   data = response.read()

with open("CmdModMoonBkside.jpg", "wb") as image_file:
    image_file.write(data)