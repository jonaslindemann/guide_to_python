# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import os

print(os.environ["PATH"])

for variable in os.environ:
    print("%s = %s" % (variable, os.environ[variable]))

os.environ["TEST"] = "Nytt värde"
print(os.environ["TEST"])
