#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:47:55 2020

@author: mc01133
"""

# decomposing a graph curve
import csv
import numpy as np
import random
import matplotlib.pylab as plt

# converting dates to computer friendly format
import datetime

def convTime(data):
         #date_time_str = data[1][0][:10]+' '+data[1][0][11:] 
    date_time_str = data
    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S')
    return date_time_obj


# select data file to open and save
def readCSV(filepath):
    csv_file = filepath
    csv_reader = csv.reader(csv_file, delimiter=',')
    data = [row for row in csv.reader(open(csv_file))]
    return data

# ---End of functions---


# fetching data files
import glob
dataFiles =(glob.glob("dati-regioni/*"))

# checking files
print('')
print('--- List of all data files: ---')
for i in range(len(dataFiles)):
    print('      ',i,'   ',dataFiles[i])

print('-------------------------------')
print('')


# make global saving array
arr1 = [[]]

inData = readCSV(dataFiles[1])
# make pockets for saving data by region
for i in range(len(inData)):
    arr1 += [[]]
    arr1[0] += [inData[1][2],inData[1][3]]
    
print('B1',len(arr1))
    
# loop through all data files
for i in range(len(dataFiles)):
    data = readCSV(dataFiles[i])
    
    # sort data into regions    
    for j in range(1,len(data)):
       
        print(i,j,[data[j][6:]])
        arr1[j] += [[data[j][6:]]]


print(arr1)        




