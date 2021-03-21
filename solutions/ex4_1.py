# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 16:41:02 2019

@author: Jonas Lindemann
"""

import os, sys

def print_path():
    """Skriv ut alla sökvägar i PATH"""
    
    if sys.platform=="win32":
        delimiter = ";"
    else:
        delimiter = ":"
        
    path_list = os.environ["PATH"].split(delimiter)
    
    for path in path_list:
        print(path)
        
if __name__ == "__main__":
    
    print_path()

