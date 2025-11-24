# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 10:21:34 2019

@author: Jonas Lindemann
"""

config = {
    "general":
        {
            "username":"olle", 
            "temp_path":"C:\\TEMP"
        },
    "constants":
        {
            "pi":3.14159,
            "g":9.82
        },
    "items":
        {
            "values": [1, 2, 3, 4, 5]
        }
}

print(config["general"]["username"])        
print(config["constants"]["pi"])
print(config["items"]["values"][1])