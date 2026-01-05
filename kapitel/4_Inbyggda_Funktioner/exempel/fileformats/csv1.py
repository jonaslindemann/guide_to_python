# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import csv

with open('example1.csv', 'r') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    for row in csv_data:
        print(row)

with open('example2.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(['Beteckning', 'Antal'])
    csv_writer.writerow(['Gurka', '2'])
    csv_writer.writerow(['Tomat', '4'])
    
l = [["Beteckning", "Antal"],["Gurka", "2"], ["Tomat", "4"]]

with open('example3.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerows(l)
