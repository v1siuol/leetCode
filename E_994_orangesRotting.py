from __future__ import annotations 
import collections 
import random 
import heapq 
import math



"""
Success
Details 
Runtime: 52 ms, faster than 91.21% of Python3 online submissions for Rotting Oranges.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Rotting Oranges.
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # brute force sim
        ret = 0
        m = len(grid)
        n = len(grid[0])
        
        rot_list = []
        fresh_set = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rot_list.append( (i,j) )
                elif grid[i][j] == 1:
                    fresh_set.add( (i,j) )

        dirt = [0,1,0,-1,0]
        while rot_list:
            if not fresh_set:
                return ret
            new_rot_list = []
            while rot_list:
                rot = rot_list.pop()
                for i in range(4):
                    new_rot = (rot[0] + dirt[i], rot[1] + dirt[i+1])
                    if new_rot in fresh_set:
                        fresh_set.remove(new_rot)
                        new_rot_list.append(new_rot)
        
            rot_list = new_rot_list
            ret += 1
            
        if not fresh_set:
            return ret
        return -1
