# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 12:56:39 2019

@author: Jonas Lindemann
"""

import csv

def read_data(filename):
    """Läs in data från CSV-fil"""
    
    with open("faithful.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, quotechar='"')

        row_number = 0

        header = []
        table = []
        
        for row in csv_reader:
            if row_number == 0:
                print(row)
                header = row
            else:
                table.append([float(v) for v in row])

            row_number +=1
    
    return header, table

def query_data(data_table, t):
    """Plocka fram utbrott längre än t"""
    
    max_table = []

    for row in data_table:
        eruption_length = row[1]
        if eruption_length>t:
            max_table.append(row)
            
    return max_table

def write_data(header, table, filename):
    """Skriv data till csv-fil"""
    
    with open(filename, "w", newline="") as csv_file:

        csv_writer = csv.writer(csv_file, delimiter=',')

        csv_writer.writerow(header)
        csv_writer.writerows(table)

        #for row in table:
        #    csv_writer.writerow(row)        

if __name__ == "__main__":
    
    header, data_table = read_data("faithful.csv")
    result_table = query_data(data_table, 4.5)

    print(result_table)

    write_data(header, result_table, "faithful_max4_5.csv")    