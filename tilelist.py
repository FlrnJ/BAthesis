#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 08:00:02 2023

@author: flurin
"""

import os
import geopandas as gpd

#%% make sure the location of this script is the working directory
wd = os.path.abspath(os.path.dirname( __file__ ) )
os.chdir(wd)
del wd

#%% read the polygons
df = gpd.read_file("data/polygons/global_mining_polygons_v2.gpkg")

#set the column called 'geometry' as the geometry of the GeoPandas
df = df.set_geometry("geometry")
df = df.to_crs("EPSG:4326")

#%%
def findtile(longitude, latitude):
    '''
    Parameters
    ----------
    longitude : float
    latitude : float

    Returns
    -------
    str
        variable with tile identifier format used in NASA's VIIRS product suite.
    '''
        
    lon = int((longitude//10) + 18)
    lat = int(8 - (latitude//10))
    
    return f'h{lon:0>2d}v{lat:0>2d}' #take care of padding the numbers

#%% ensure the function is correct
test_list = []

lon = range(-180,180, 5)
lat = range(-90, 90, 5)

for i in range(72):
    for j in range(36):
        test_list.append(f'for lon:{lon[i]} and lat:{lat[j]} the corresponding tile is:{findtile(lon[i], lat[j])}')

del i,j,lon,lat
print('Check the new variable "test_list"')
#%%

tilelist = []

for i in range(len(df)):
    ext_values = df.iloc[i]['geometry'].bounds

    tileID = list(set((findtile(ext_values[0], ext_values[1]), findtile(ext_values[2], ext_values[3]))))
    tilelist.append(tileID)
    
df['tileID'] = tilelist
del i, ext_values, tileID
#%%
df.to_csv('data/dataframes/df_tilelist.csv',index=False)











