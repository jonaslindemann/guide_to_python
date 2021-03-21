# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 12:56:39 2019

@author: Jonas Lindemann
"""

def read_data(filename):
    """Läs in data från CSV-fil"""
    
    with open("faithful.csv", "r") as csv_file:
        lines = csv_file.readlines()
    
    header = lines[0]
    data_lines = lines[1:]
    
    data_table = []
    
    for line in data_lines:
        items = line.split(",")
        
        idx = int(items[0])
        eruption_length = float(items[1])
        eruption_wait = float(items[2])
        
        data_table.append([idx, eruption_length, eruption_wait])
        
    return header, data_table

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
    
    with open(filename, "w") as csv_file:
        csv_file.write(header)
        
        for row in table:
            for i in range(len(row)):
                if i<2:
                    csv_file.write(str(row[i])+", ")
                else:
                    csv_file.write(str(row[i])+"\n")
        

if __name__ == "__main__":
    
    header, data_table = read_data("faithful.csv")
    result_table = query_data(data_table, 4.5)
    write_data(header, result_table, "faithful_max4_5.csv")    