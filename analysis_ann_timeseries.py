#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 23:05:30 2022

@author: flurin
"""
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#%% load data

data = pd.read_csv('ann_ntl_emiss_2012-2021.csv')
df = data.drop(['Unnamed: 0', 'geometry'], axis=1)

#%% grouping by country, averaging and removing countries with few samples
ctry_grp = df.groupby(['COUNTRY_NAME']).mean() #.sum(numeric_only=True)

ctry_grp['n_mines'] = df.groupby(['COUNTRY_NAME']).size()

ctry_grp1 = df.groupby(['COUNTRY_NAME']).sum(numeric_only=True)
ctry_grp['total_AREA'] = ctry_grp1['AREA']

ctry_grp = ctry_grp[ctry_grp['n_mines']>30]


#%% number of mines and area of mines in top10 'brightest' countries
top10 = ctry_grp.iloc[ctry_grp['n_mines'].argsort()[-10:]]
#top10 = top10[::-1]

fig0, axes0 = plt.subplots(2,1, figsize=(15,12))


for i in range(len(top10)):
    ctry0 = top10.iloc[i].name
    values0 = top10.iloc[i]['n_mines']
    axes0[0].bar(ctry0, values0, label=f'{ctry0}', linewidth=3)
    
    axes0[0].set_title('Total n of Mines in top 10 countries')
    axes0[0].set_ylabel('number of mines')


for i in range(len(top10)):
    ctry1 = top10.iloc[i].name
    values1 = top10.iloc[i]['total_AREA']
    axes0[1].bar(ctry1, values1, label=f'{ctry1}', linewidth=3)
    
    axes0[1].set_title('Total area of mines')
    axes0[1].set_ylabel('area')

#%% development top10 countries

x = np.arange(2012, 2022, dtype=int)
#top10 = top10[::-1]


fig1, axes1 = plt.subplots(2,1, figsize=(15.5,17))

for i in range(len(top10)):
    ctry = top10.iloc[i].name
    values = top10.iloc[i][1:11].squeeze()
    axes1[0].plot(x, values, label=f'{ctry}', linewidth=3)
    
axes1[0].set_title('Average nighttime light emissions')
axes1[0].set_xlabel('year')
axes1[0].set_ylabel('brightness (nWatts·cm^(−2)·sr^(−1))')
axes1[0].legend()

for i in range(len(top10)):
    ctry = top10.iloc[i].name
    values = top10.iloc[i][1:11].squeeze() / top10.iloc[i][1]
    axes1[1].plot(x, values, label=f'{ctry}', linewidth=3)
    
axes1[1].set_title('Indexed average nighttime light emissions')
axes1[1].set_xlabel('year')
axes1[1].set_ylabel('change in brightness (nWatts·cm^(−2)·sr^(−1))')
axes1[1].legend()

#%% plot a set of randomly selected mines
rng = np.random.default_rng()

fig2, axes2 = plt.subplots(1,1, figsize=(10,8))

for i in range(10):
    rand_mine = rng.integers(len(df))
    values = df.iloc[rand_mine][3:13].squeeze()
    axes2.plot(x, values, linewidth=2, label=f'ID {df.iloc[rand_mine].name}, {df.iloc[rand_mine][0]}')
    
    axes2.set_title('Average nighttime Light emissions of randomly slected mines')
    axes2.set_xlabel('year')
    axes2.set_ylabel('brightness (nWatts·cm^(−2)·sr^(−1))')
    axes2.legend()