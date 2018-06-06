#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 21:14:17 2018

@author: zhengcao
"""

'''
approach 4
'''
#class Solution:
#    def allPathsSourceTarget(self, graph):
#        frontier = [(0, ())]
#        paths = []
#        N = len(graph)
#        while len(frontier):
#            node, path = frontier.pop()
#            path = path + (node, )
#            if node == N - 1:
#                paths += [path]
#            else:
#                for neighbor in graph[node]:
#                    frontier.append((neighbor, path))
#        return paths

'''
approach 3
'''
class Solution:            
    
    def allPathsSourceTarget(self, graph):
        r, LAST = [], len(graph) - 1
        def go(i, path):
            if i == LAST:
                r.append(path)
                return
            for j in graph[i]:
                go(j, path + [j])
        go(0, [0])
        return r

'''
approach 1

The philosophy behind dynamic programming is successfully applied in this method.
paths[k] = paths[m] + edge(m, k) over all node m that is incident to k. 

'''
#class Solution:            
#    
#    def allPathsSourceTarget(self, graph):
#        N = len(graph) - 1
#        
#        def solve(node):
#            if node == N:
#                return [[N]]
#            else:
#                paths = []
#                for neighbors in graph[node]:
#                    for path in solve(neighbors):
#                      paths.append([node] + path)
#                return paths
#
#        return solve(0)

'''
appraoch 2

The approach searches all possible paths from 0 to N-1 with the method of DFS
'''
        
#class Solution:
#    
#    def DFS(self, parentNode):
#        if parentNode == len(self.graph) - 1:
#            self.currentPath.append(parentNode)  
#            self.paths.append(self.currentPath.copy())
#            del self.currentPath[-1]
#        else: 
#            self.mark[parentNode] = 1
#            self.currentPath.append(parentNode)
#        
#            
#            for child_node in self.graph[parentNode]:                
#                if self.mark[child_node] == 0:
#                    self.DFS(child_node)
#            
#            self.mark[parentNode] = 0
#            del self.currentPath[-1]
#            
#    
#    def allPathsSourceTarget(self, graph):
#        self.mark = [0] * len(graph)
#        self.graph = graph
#        self.currentPath = []
#        self.paths = []
#        
#        self.DFS(0)
#        
#        return self.paths  

if __name__ == '__main__':
    graph = [[1, 2], [3], [3], []]
    
    s = Solution()
    paths = s.allPathsSourceTarget(graph)
    print(paths)
    
#    print((1, (1, 2)))
    