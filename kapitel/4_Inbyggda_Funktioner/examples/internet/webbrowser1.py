# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""
import webbrowser as browser

url = 'http://docs.python.org/'

# Open URL in a new tab, if a browser window is already open.
browser.open_new_tab(url)

# Open URL in new window, raising the window if possible.
browser.open_new(url)