from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 1132 ms, faster than 88.89% of Python3 online submissions for Number Of Corner Rectangles.
Memory Usage: 15 MB, less than 45.71% of Python3 online submissions for Number Of Corner Rectangles.
"""

class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        # TLE 
        # ret = 0
        # for i in range(len(grid)-1):
        #     for j in range(i+1, len(grid)):
        #         c = 0
        #         for k in range(len(grid[0])):
        #             if grid[i][k] == grid[j][k] == 1:
        #                 c += 1
        #         ret += c * (c-1) // 2
        # return ret 
        
        m = len(grid)
        n = len(grid[0])
        res = 0
        dp = [[0] * n for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for q in range(j+1, n):
                        if grid[i][q] == 1:
                            res += dp[j][q]
                            dp[j][q] += 1
        return res 
