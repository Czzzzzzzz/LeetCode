#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 17:34:31 2018

@author: zhengcao
"""
import numpy as np
import math

class PriorityQueue:
    
    #data structure aimed to store elements.
    # __ means a private method or an attribute
    __heapArray = np.array([])
    __size = 0
    __number = 0
    
    def __init__(self, size):
        self.__heapArray = np.zeros(size)
        self.__size = size
        
    def __heapify_up(self, position):
        element = self.__heapArray[ position ]
        parent_pos = math.ceil ( position / 2 - 1)
        
        if position == 0:
            return 
        
        if self.__heapArray[ parent_pos ] > element:
            self.__heapArray[ position ], self.__heapArray[ parent_pos ] = self.__heapArray[ parent_pos ],self.__heapArray[ position ]        
    
            self.__heapify_up(parent_pos)
        else:
            return

        
    def __heapify_down(self, position):
        element = self.__heapArray[ position ]
        left_child_pos = position * 2 + 1
        right_child_pos = position * 2 + 2
        
        if left_child_pos > self.__number:
            return
        
        elif left_child_pos == self.__number:
            child_pos = left_child_pos
            
        else:
            if self.__heapArray[ left_child_pos ] < self.__heapArray[ right_child_pos ]:
                child_pos = left_child_pos
            else:
                child_pos = right_child_pos
        
        if self.__heapArray[ child_pos ] < element :
            self.__heapArray[ position ], self.__heapArray[ child_pos ] = self.__heapArray[ child_pos ], self.__heapArray[ position ]        
            self.__heapify_down( child_pos )
            
        else:
            return
        
        
        
    def __insert(self, element):
        
        if self.__number >= self.__size:
            print ("queue is full")
            return 
        
        self.__heapArray[self.__number] = element
        self.__heapify_up(self.__number)
        
        self.__number = self.__number + 1
        
    def __delete(self, position):
        self.__number = self.__number - 1
        
        ele = self.__heapArray[position]
        self.__heapArray[position] = self.__heapArray[ self.__number ]
        
        if position == 0:
            self.__heapify_down(position)
        else:
            parent_pos = math.ceil ( position / 2 - 1)
            if self.__heapArray[parent_pos] > self.__heapArray[position]:
                self.__heapify_up(position)
            else:
                self.__heapify_down(position)                

        return ele
        
    def pop(self):
        return self.__delete(0)
        
    def push(self, element):
        self.__insert(element)
    
    def testFunction(self):
        print("helllo world")
        print(self.__number)

    def printHeap(self):
        for i in range(0, self.__number):
            print(self.__heapArray[i])


def swap(a, b):
    temp = a
    a = b
    b = temp

def main():
    t = PriorityQueue(5)

    t.push(10)
    t.push(3)
    t.push(1)
    t.push(11)
    t.push(5)
    
    t.printHeap()
    
    print("pop testing:")
    t.pop()
    t.pop()
    t.printHeap()
    
    print("push testing 2:")
    t.push(9)
    t.printHeap()
    

if __name__ == "__main__":
    main()