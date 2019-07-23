from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 168 ms, faster than 5.01% of Python3 online submissions for Max Area of Island.
Memory Usage: 16.4 MB, less than 28.57% of Python3 online submissions for Max Area of Island.
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs O(m*n)
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(grid, i, j))

        return max_area



def dfs(grid, x, y):
    c = 1
    grid[x][y] = 0
    directions = [0,1,0,-1,0]
    for d in range(4):
        new_x = x + directions[d]
        new_y = y + directions[d+1]
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 1:
            c += dfs(grid, new_x, new_y)
    return c 
