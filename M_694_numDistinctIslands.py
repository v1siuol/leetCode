from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 212 ms, faster than 97.61% of Python3 online submissions for Number of Distinct Islands.
Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Number of Distinct Islands.
"""
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # distince island + shape recognization
        # one pass (n w log w) time O(n) space
        shapes = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temp_island = []
                if grid[i][j] == 1:
                    dfs(grid, i, j, temp_island)
                    shapes.add(cast_island(temp_island))
        return len(shapes)
                    
def dfs(grid, i, j, temp_island):
    if grid[i][j] == 0:
        return 

    grid[i][j] = 0
    temp_island.append( (i, j) )
    if i - 1 >= 0:
        dfs(grid, i-1, j, temp_island)
    if i + 1 <= len(grid) - 1:
        dfs(grid, i+1, j, temp_island)
    if j - 1 >= 0:
        dfs(grid, i, j-1, temp_island)
    if j + 1 <= len(grid[0]) - 1:
        dfs(grid, i, j+1, temp_island)

def cast_island(temp_island):
    dx, dy = temp_island[0]
    return tuple(sorted([(x-dx, y-dy) for x, y in temp_island]))

