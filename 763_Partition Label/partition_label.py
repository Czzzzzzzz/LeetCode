#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 20:07:17 2018

@author: zhengcao
"""

import numpy as np

'''
Solution 1
'''

#class Solution(object):
#    def partitionLabels(self, S):
#        last = {c: i for i, c in enumerate(S)}
#        j = anchor = 0
#        ans = []
#        for i, c in enumerate(S):
#            j = max(j, last[c])
#            if i == j:
#                ans.append(i - anchor + 1)
#                anchor = i + 1
#            
#        return ans

'''
Solution 2
'''

class Solution:
    def partitionLabels(self, S):
        str_part = np.array([-1] * len(S)) 
        char_part = {}

        max_par_num = 0
        
        for char, i in zip(S, range(len(S))):
            if char in char_part:
                part_num = char_part[char]
                for j in range(i):
                    if str_part[j] > part_num:
                        str_part[j] = part_num
                        char_part[S[j]] = part_num
                str_part[i] = part_num
            else:
                max_par_num += 1
                char_part[char] = max_par_num
                str_part[i] = max_par_num
        
        print(str_part)
        print(char_part)
        
        split_points = [0]
        for i in range(1, str_part.shape[0]):
            if str_part[i] != str_part[i-1]:
                split_points.append(i)
        split_points.append(len(S))
        print(split_points)
        
        results = [S[split_points[i-1]:split_points[i]] for i in range(1, len(split_points))]
        size = [len(substr) for substr in results]
        return size
                
        
if __name__ == '__main__':
#    test_str = 'ababcbacadefegdehijhklij'
#    s = Solution()
#    results = s.partitionLabels(test_str)
#    print(results)
    
#    a = np.arange(10)
#    s = 'aasffg'

#    print(np.split(s, [2, 3]))
#    a = np.array([5, 1, 2, 2, 3, 3, 5, 5])
#    b = np.bincount(a)
#    c = np.nonzero(b)
#    print(b[c])
    
    
    
    
    
    
    
    
    
    
    
    