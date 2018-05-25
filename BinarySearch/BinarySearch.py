#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 15:28:27 2018

@author: zhengcao
"""

class BinarySearch:
    
    def binary_search(self, array, element):
        sorted_array = sorted(array)
        return self.__search(sorted_array, 0, len(array)-1, element)
        
    def __search(self, array, startAt, endAt, element):
        
        if startAt > endAt:
            return False
        
        mid = int((startAt + endAt) / 2)

        if array[mid] == element:
            return True
        elif array[mid] > element:
            return self.__search(array, startAt, mid-1, element)
        else:
            return self.__search(array, mid+1, endAt, element)
                
            
        
        
if __name__ == "__main__":
    s = BinarySearch()
    print(s.binary_search([1, 2, 3, 4, 5, 6, 7], 0))