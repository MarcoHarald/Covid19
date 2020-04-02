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
    
# loop through all data files
inData = readCSV('dati-regioni/dpc-covid19-ita-regioni.csv')

# make pockets for saving data by region
for i in range(1,21):
    arr1 += [[]]
    arr1[0] += [[i]]

for i in range(len(inData[0])):
    print('      ',i,'   ',inData[0][i])
print('----------------------')
print()

# convert dates to datetime
for i in range(1,len(inData)):
    inData[i][0] = convTime(inData[i][0])

print('Numb. Region data days :   ',len(inData))
print('Numb. Regions          :   ',len(inData[1])+1)

# sort data into regions    
for j in range(1,len(inData)):
    # check region ID, select approapriate
    regionID = int(inData[j][2])
    arr1[regionID] += [inData[j]]
            
# make plot of a single region


# plot ------------------------------------------------------------------------------------------------

targetRegion = 1
targetDataTypes = [10]

for targetDataType in targetDataTypes:
    for j in range(5):
        targetRegion = j
        print(targetDataType, targData)
        
        # target region data
        targData = arr1[targetRegion]
        
        t = []
        ax = []
        
        # make a plot line: loop through a single data type for a single region
        for i in targData:
            t += [i[0]]
            ax += [int(i[targetDataType])]
        
        # set data type & region names
        plt.plot(t, ax, label=inData[0][targetDataType]+'_'+inData[targetRegion][3])

plt.legend(loc='upper left')
plt.ylabel('Price ($)', fontsize=10)
plt.xlabel('Time (days)', fontsize=10)
plt.show()




