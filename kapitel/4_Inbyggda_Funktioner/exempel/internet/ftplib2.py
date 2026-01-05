# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

# ftp://goes.gsfc.nasa.gov/pub/goeswest/san_francisco/maps/

# ftp://goes.gsfc.nasa.gov/pub/goeswest/san_francisco/vis/

#ftp://spdf.gsfc.nasa.gov/pub/ 

#/pub/data/image/hk/ads_k0/2005/im_hk_ads_20050101_v01.cdf

from email.mime import image
import ftplib
import cdflib
import numpy as np
from PIL import Image  # or use matplotlib

with ftplib.FTP_TLS() as ftp:
    ftp.connect("nssdcftp.gsfc.nasa.gov", 21)
    ftp.login("anonymous", "")
    print(ftp.getwelcome())
    print(ftp.pwd())

    ftp.cwd("/pub/data/image/hk/ads_k0/2005")
    # print(ftp.pwd())

    file_list = ftp.nlst()
    print(len(file_list))

    image_filename = file_list[-1]

    print("Downloading", image_filename)

    with open(image_filename, 'wb') as image_file:
        ftp.retrbinary('RETR '+image_filename, image_file.write)

cdf_file = cdflib.CDF(image_filename)
file_info = cdf_file.cdf_info()
for item in file_info.zVariables:
    print(item)