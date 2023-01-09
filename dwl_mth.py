#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 19:03:46 2023

@author: flurin
"""
import os

#%% Lists for downloads and folder structure 
tiles = ['h33v12', 'h09v05', 'h20v05']

years = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
months = ['001', '032', '061', '092', '122', '153', '183', '214', '245', '275', '306', '336']

#%% make folder structure

for i in range(len(years)):
    parent_dir = '/Users/flurin/Library/CloudStorage/OneDrive-Personal/Dokumente/HSG/BaTh/BAthesis-main/monthlydata/data'

    directory = years[i]
        
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    
    parent_dir = path
    
    for j in range(len(months)):
        directory = months[j]
        
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        
#%% fetch data from server

TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBUFMgT0F1dGgyIEF1dGhlbnRpY2F0b3IiLCJpYXQiOjE2NzMyMTA5NTAsIm5iZiI6MTY3MzIxMDk1MCwiZXhwIjoxNjg4NzYyOTUwLCJ1aWQiOiJmbHJuIiwiZW1haWxfYWRkcmVzcyI6ImZsdXJpbi5qYWNvbWV0QGdtYWlsLmNvbSIsInRva2VuQ3JlYXRvciI6ImZscm4ifQ.i8k3zpmf7TxMpH0-r9H4TkHp-NpSq9sW1Ld7HpBxcjE' #check the NASA LAADS archive login website to generate token

print('-'*50, '\nThe download started. Please wait.\n', '-'*50)

for y in range(len(years)): #len(year)
    year = years[y]
    
    for m in range(len(months)): #len(month)
        month = months[m]
        
        for t in range(len(tiles)):
            tile = tiles[t]
            
            PATH_TO_DATA_DIRECTORY = '"https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5000/VNP46A3/' + year +'/' + month + '/"' #5000 is the number for the VIIRS dataset #VNP46A4 is yearly aggregated data
            TARGET_DIRECTORY_ON_YOUR_FILE_SYSTEM = '/Users/flurin/Library/CloudStorage/OneDrive-Personal/Dokumente/HSG/BaTh/BAthesis-main/monthlydata/data/' + year + '/' + month

            cmd = 'wget -e robots=off -m -np -R .html,.tmp -A "*' + tile + '*" -nH --cut-dirs=6 ' + PATH_TO_DATA_DIRECTORY + ' --header "Authorization: Bearer ' + TOKEN + '" -P ' + TARGET_DIRECTORY_ON_YOUR_FILE_SYSTEM

            os.system(cmd)

print('-'*50, '\nThe download is completed.\n', '-'*50)
