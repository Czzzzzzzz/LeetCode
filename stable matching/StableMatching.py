#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 10:51:57 2018

@author: zhengcao
"""
import numpy as np


def readPreferenceList(filename):
    number = int(open(filename, 'r').readline())
    PreferenceList = np.loadtxt(filename, dtype=np.int8, skiprows = 1)

    print(PreferenceList)
    
    MPreList, WPreList = np.split(PreferenceList, 2, axis = 0)
    print("man preference list")
    print( MPreList )
    print("woman preference list")
    print( WPreList )
    
    return number, MPreList, WPreList

def isAllEngaged(ManStatus):
    for i in range(ManStatus.shape[0]):
        if ManStatus[i] == 0:
            return i
    return -1

def createRankingList(WPreList):
    manRanking = np.zeros(WPreList.shape)
    for r in range(0, WPreList.shape[0]):
        weigh = 0
        for c in range(0, WPreList.shape[1]):    
            manRanking[r, WPreList[r, c]] = weigh
            weigh = weigh - 1
    
    return manRanking

def main():
    number, MPreList, WPreList = readPreferenceList("preferencelist2.data")
    ManStatus = np.zeros(number, dtype=np.int8)            #if manStatus[i] == 0, ith man is not engaged. If manStatus[i] == 1, opposite.
    WomanStatus = np.zeros(number, dtype=np.int8)
    engagement = np.zeros(number, dtype=np.int8)           #index is woman number, value is man number
    Next = np.zeros(number, dtype=np.int8)                 #Next[i] denotes ith ranking woman to whom man will propose

    manRanking = createRankingList(WPreList)
    
    print("man ranking matrix")
    print(manRanking)
    
    manIndex = isAllEngaged(ManStatus)
    while ( manIndex != -1 ):
        proposedWoman = MPreList[manIndex, Next[manIndex]]
        
        if ( WomanStatus[proposedWoman] == 0 ):
            ManStatus[manIndex] = 1
            WomanStatus[proposedWoman] = 1
            engagement[proposedWoman] = manIndex
        else:
            engagedMan = engagement[proposedWoman]
            if manRanking[proposedWoman, manIndex] > manRanking[proposedWoman, engagedMan]:
                engagement[proposedWoman] = manIndex
                ManStatus[engagedMan] = 0
                ManStatus[manIndex] = 1
        Next[manIndex] += 1
        
        manIndex = isAllEngaged(ManStatus)
    
    print("result:")
    for i in range(number):
        print("woman " + str(i) + " match man " + str(engagement[i]))

if __name__ == "__main__":
    main()