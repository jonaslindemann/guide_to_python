# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()

with open("page.html", "w") as html_file:
    html_file.write(html.decode("utf-8"))
    
#html_file.write()