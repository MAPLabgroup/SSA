# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 09:56:13 2020

@author: jancy
"""


import pandas as pd
import numpy as np
import os.path as op
import glob
import re
import matplotlib
import matplotlib.pyplot as plt



envgoals = {'env1': {'face': 'George_Clooney', 'food': 'lettuce', 'animal': 'zebra'},
		 'env5': {'face': 'Oprah_Winfrey', 'animal': 'giraffe', 'tool': 'hammer'},
		 'env8': {'face': 'Elvis_Presley', 'animal': 'brown_bear', 'food': 'oranges'},
		 'env10': {'face': 'Queen_Elizabeth_II', 'animal': 'alligator', 'tool': 'drill'},
		 'env11': {'face': 'Marilyn_Monroe', 'tool': 'scissors', 'animal': 'duck'},
		 'env12': {'face': 'Paul_McCartney', 'animal': 'cow', 'food': 'apple'}
		 }

def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys

# d2 = pd.DataFrame() 

# test_files = glob.glob(op.join('C:\\Users\\jancy\\Documents\\MAP_RA\\SSA\\SSAO Analysis\\testing\\ssa002\\run1\\session_19_10_03_10_17', 'log.txt'))

n_runs = 6

for run_num in range(1, n_runs+1):
    test_files = glob.glob(op.join('C:\\Users\\jancy\\Documents\\MAP_RA\\SSA\\SSAO Analysis\\testing\\ssa002',\
                                           'run'+ str(run_num),\
                                           'session_*', 'log.txt'))
    
    for i, test_files in enumerate(test_files):
        if i > 0: print ('***** something happened, '+str(i+1)+' files for run ' +str(run_num)+'! *****')
        
    # open and read the file 
    f = open(test_files)
    data1 = f.readlines()
    output = []
    for line in data1:
        columns = re.split('\t|\r|\n', line)
        output.append(columns)

    d1 = pd.DataFrame(output, columns = ['time', 'c2', 'command', 'c3', 'c4', 'c5', 'c6', 'c7'])

    d1.time = d1.time.astype('int64')/1000
    session_start = d1.time.min()
    d1.time = d1.time - session_start

    # get rid of some unnessary stuff
    d2 = d1.loc[d1.command.isin(['VROBJECT_POS', 'VROBJECT_HEADING', 'INPUT_EVENT','ORIENT', 'ARRIVED', 'ASSIGNED', 'NAVIGATE', 'SCAN', 'SHOCK'])]
    d2.drop(['c2', 'c5', 'c6', 'c7'], axis=1, inplace=True) #unneeded cols


    counts = d2.groupby('command').count()
    counts = counts['time']['ORIENT']
    print (counts)

    # get orient onsets to seperate each trail
    d2.sort_values(by='time', inplace=True) # make sure sorted by time! this can be weird w/crashes
    orient_onsets = d2.loc[d2.command == "ORIENT"]
    orient_onsets['trial'] = 0 # init trial number

    # assign trail number
    for counter, ind in enumerate(orient_onsets.index):
            if counter == 0: # first trial
                first_ind = ind
                orient_onsets.loc[ind, 'trial'] = 1
                prev_ind = ind  
            else:
                orient_onsets.loc[ind, 'trial'] = orient_onsets.loc[prev_ind, 'trial'] + 1
                prev_ind = ind

    # experiment trial-segment onsets
    onset_times = d2.loc[d2.command.isin(['ORIENT', 'ASSIGNED', 'NAVIGATE', 'SHOCK', 'ARRIVED'])]

    # prune "ARRIVED" if not to a target (eg if run into sub-goal)
    targets = ['ZZZ', 'George_Clooney', 'Oprah_Winfrey', 'Elvis_Presley', \
                   'Queen_Elizabeth_II', 'Marilyn_Monroe',\
                   'Paul_McCartney']
        
    arrived_times = d2.loc[(d2.command == 'ARRIVED') & (d2.c3.isin(targets))]


    # Get 2D position in space
    dp = d2.loc[d2.command == 'VROBJECT_POS'].reset_index()
    coordinates = pd.DataFrame(dp.c4.str.split('Point3|, |\(|\)').tolist())[[2, 3, 4]]
    coordinates.rename(columns={2: 'x', 3: 'y', 4: 'z'}, inplace=True)
    dp = dp.join(coordinates)
    dp[['x', 'y', 'z']] = dp[['x', 'y', 'z']].astype(float)

    # dp2 = downsample_sec_reindex(dp, rate='500L'), what is this function for ?

    dp = dp.loc[dp.c3 == 'PandaEPL_avatar'] # remove positions that aren't actually navigator

     # keyboard events
    keyboard_events = d1.loc[d1.command.isin(['KEYBOARD_DOWN', 'KEYBOARD_UP'])]
    keyboard_events.drop(['c2', 'c5', 'c6', 'c7'], axis=1, inplace=True) #unneeded cols

    # Get heading direction
    dh = d2.loc[d2.command == 'VROBJECT_HEADING'].reset_index()

    # Get input events (holding down button)
    di = d2.loc[d2.command == 'INPUT_EVENT'].reset_index()

    data = pd.concat([onset_times, keyboard_events, dp, dh, di]).sort_index()

    data.sort_values(by='index', inplace=True)

# plotting function
# find environment 

    allgoals = ['George_Clooney', 'Oprah_Winfrey', 'Elvis_Presley', \
                   'Queen_Elizabeth_II', 'Marilyn_Monroe',\
                   'Paul_McCartney']

    test2 = d2.loc[(d2.command == 'VROBJECT_POS') & (d2.c3.isin(allgoals))]


    dictOfWords = {
    "env1": 'George_Clooney',
    "env5" : 'Oprah_Winfrey' ,
    "env8" : 'Elvis_Presley',
    "env10" : 'Queen_Elizabeth_II',
    "env11" : 'Marilyn_Monroe',
    "env12" : 'Paul_McCartney'
    }


    buildings = pd.read_csv('C:\\Users\\jancy\\Documents\\MAP_RA\\SSA\\SSAO Analysis\\building_coords.csv')
    goals = pd.read_csv('C:\\Users\\jancy\\Documents\\MAP_RA\\SSA\\SSAO Analysis\\item_coordinates.csv')
    
    for i in range(0,3):
        index1 = test2.index[i]
        listOfKeys = getKeysByValue(dictOfWords, test2.loc[index1, 'c3'])
        for key in listOfKeys:
             print(key)
             coords = buildings[buildings.env == key]
             goal = goals[goals.env == key ]
             time1 = arrived_times.index[0]
             time2 = arrived_times.index[1]
             time3 = arrived_times.index[2]
             time = arrived_times.index[i]
             if time == time1 :
                 path = dp[(dp.c3 == 'PandaEPL_avatar') & (dp.time <= arrived_times.loc[time1, 'time']) ]
             elif time == time2 :
                 path = dp[(dp.c3 == 'PandaEPL_avatar') & (dp.time > arrived_times.loc[time1, 'time']) & (dp.time <= arrived_times.loc[time2, 'time']) ]
             else:
                 path = dp[(dp.c3 == 'PandaEPL_avatar') & (dp.time > arrived_times.loc[time2, 'time']) ]
        
        fig, ax = plt.subplots(figsize = (4,4))
        ax.set_xlim(0, 60)
        ax.set_ylim(0, 60)
        ax.scatter(coords.x, coords.y, s=25, alpha=0.7, marker='.', color='gray')
        ax.scatter(goal.x, goal.y, s=30, alpha=0.7, marker='o', color='orange')
        ax.scatter(path.x, path.y, s=1, alpha=0.7, marker='o', color='blue')
        ax.set_title(key)
        plt.show()       
                
                 