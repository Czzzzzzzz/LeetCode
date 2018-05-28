#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#Created on Thu May 24 20:37:05 2018

@author: zhengcao
"""

#import math

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def __MaxBinaryTree(self, nums):
        if nums:
            maxVal = max(nums)
            maxIndex = nums.index(maxVal)            
            parentNode = TreeNode(maxVal)
            parentNode.left = self.__MaxBinaryTree(nums[:maxIndex])
            parentNode.right = self.__MaxBinaryTree(nums[maxIndex+1:])
            
#            print(parentNode.val)
            
            return parentNode
    
    
    def constructMaximumBinaryTree(self, nums):
        
        head = self.__MaxBinaryTree(nums)        
        
        return head  
    
#   solution 2: The basic flow is same with the solution 1, which, however, is more concise and
#               takes advantage of features of list in python
        
#    def __MaxBinaryTree(self, left, right):
#        if left >= right:
#            return None
#        else:
#            maxVal = max(self.nums[left:right])
#            maxIndex = self.nums.index(maxVal)
#            leftNode = self.__MaxBinaryTree(left, maxIndex)
#            rightNode = self.__MaxBinaryTree(maxIndex+1, right)
#            
#            parentNode = TreeNode(maxVal)
#            parentNode.left = leftNode
#            parentNode.right = rightNode
#            
##            print(parentNode.val)
#            
#            return parentNode
#    
#    
#    def constructMaximumBinaryTree(self, nums):
#        self.nums = nums
#        
#        head = self.__MaxBinaryTree(0, len(nums))        
#        
#        return head
    
    def __midOrderTransverse(self, node):
        if node is not None:
            self.__midOrderTransverse(node.left)
            print(node.val)
            self.__midOrderTransverse(node.right)
    
    def tranverseNodes(self, head):
        self.__midOrderTransverse(head)

if __name__ == "__main__":
    a = [3, 2, 1, 6, 0, 5]
#    s = Solution()
#    head = s.constructMaximumBinaryTree(a)
#
#    s.tranverseNodes(head)
    
    if a[2:1]:
        print("null")
    else:
        print("not null")

