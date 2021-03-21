# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 12:16:54 2019

@author: Jonas Lindemann
"""

import pathlib as pl

def find_all_files(path):
    """Lista alla filer i path"""
    
    p = pl.Path(path)
    
    file_list = []
    
    for x in p.iterdir():
        if x.is_file():
            file_list.append(x)
            
    return file_list

if __name__ == "__main__":
    
    file_list = find_all_files(pl.Path.cwd())
    
    for file in file_list:
        print(file)