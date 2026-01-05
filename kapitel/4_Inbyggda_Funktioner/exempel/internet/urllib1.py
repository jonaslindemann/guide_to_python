# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import urllib.request
import gzip
from io import BytesIO
from PIL import Image

# Create a request with a User-Agent header to avoid 403 Forbidden
url = r'https://upload.wikimedia.org/wikipedia/commons/1/18/C65alleine_%28no_bg%29_%28balance%29.jpg'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

with urllib.request.urlopen(req) as response:
   jpeg = response.read()

# Decode JPEG directly from bytes without writing to file
image = Image.open(BytesIO(jpeg))
print(f"Image size: {image.size}")
print(f"Image format: {image.format}")
print(f"Image mode: {image.mode}")

# Now you can work with the image object directly
image.show()  # Display the image
#image.save("c65.jpg")  # Save if needed