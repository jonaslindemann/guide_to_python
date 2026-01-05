# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 12:22:58 2019

@author: Jonas Lindemann
"""

import configparser

config = configparser.ConfigParser()

config["DEFAULT"] = {
        "Rating":"No rating",
        "Length":"No length"
        }

config["Dr Who"] = {"Rating":"9/9"}
config["Firefly"] = {"Length":"Too long"}

with open("config3.ini", "w") as config_file:
    config.write(config_file)
    

