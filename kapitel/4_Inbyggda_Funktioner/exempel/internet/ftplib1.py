# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import ftplib

with ftplib.FTP("ftp.acc.umu.se") as ftp:
    ftp = ftplib.FTP("ftp.acc.umu.se")
    ftp.login()
    print(ftp.getwelcome())
    print(ftp.dir())
    print(ftp.nlst())
    print(ftp.pwd())    
    

