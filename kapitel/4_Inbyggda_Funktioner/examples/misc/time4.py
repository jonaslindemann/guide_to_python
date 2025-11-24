# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import datetime

todays_date = datetime.date.today()
print(todays_date)

old_date = datetime.date(2001, 12, 31)

diff = todays_date - old_date
print(diff.days)

print(old_date)
print(todays_date.weekday())
print(todays_date.timetuple())

time_format = '%a, %d %b %Y %H:%M:%S'
print(todays_date.strftime(time_format))

