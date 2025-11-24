# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

# ftp://goes.gsfc.nasa.gov/pub/goeswest/san_francisco/maps/

# ftp://goes.gsfc.nasa.gov/pub/goeswest/san_francisco/vis/

import ftplib

with ftplib.FTP("neoftp.sci.gsfc.nasa.gov") as ftp:
    ftp.login()
    print(ftp.getwelcome())
    ftp.cwd("/rgb/VIIRS_543D/")
    print(ftp.pwd())

    file_list = ftp.nlst()
    print(len(file_list))

    image_filename = file_list[-1]

    print("Downloading", image_filename)

    with open(image_filename, 'wb') as image_file:
        ftp.retrbinary('RETR '+image_filename, image_file.write)
