#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:50:27 2018

@author: zhengcao
"""

import math 

class Solution:
    def findDuplicates(self, nums):
        
        result = []        
        for i in range(0, len(nums)):
            index = int(math.fabs(nums[i])) - 1
            if nums[index] < 0:
                result.append(index + 1)
            else:
                nums[index] = -nums[index]
        
        return result
    
if __name__ == "__main__":

    test = [7, 3, 2, 4, 8, 2, 3, 1]
    
    s = Solution()
    print(s.findDuplicates(test))