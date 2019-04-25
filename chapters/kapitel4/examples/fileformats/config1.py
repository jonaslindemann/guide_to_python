# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 12:22:58 2019

@author: Jonas Lindemann
"""

import configparser

config = configparser.ConfigParser()
config.read("config1.ini")

sections = config.sections()
print(sections)

print(config["bitbucket.org"]["user"])

for section in config.sections():
    print("section =", section)
    keys = config[section].keys()
    for key in keys:
        print(key, "=", config[section][key])
        
config["bitbucket.org"]["user"] = "jonas"
print(config["bitbucket.org"]["user"])

with open("config2.ini", "w") as config_file:
    config.write(config_file)
