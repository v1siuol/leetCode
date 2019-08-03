from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 1264 ms, faster than 8.33% of Python3 online submissions for Cherry Pickup.
Memory Usage: 13.8 MB, less than 76.92% of Python3 online submissions for Cherry Pickup.
"""

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # ??? 
        n = len(grid)
        m = n * 2 - 1
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = grid[0][0]

        for i in range(1, m):
            for j in range(n)[::-1]:
                for k in range(n)[::-1]:
                    p = i - j
                    q = i - k

                    if p < 0 or p >= n or q < 0 or q >= n or grid[j][p] < 0 or grid[k][q] < 0:
                        dp[j][k] = -1
                        continue

                    if j > 0:
                        dp[j][k] = max(dp[j][k], dp[j-1][k])
                    if k > 0:
                        dp[j][k] = max(dp[j][k], dp[j][k-1])
                    if j > 0 and k > 0:
                        dp[j][k] = max(dp[j][k], dp[j-1][k-1])
                    if dp[j][k] >= 0:
                        dp[j][k] += grid[j][p] + (grid[k][q] if j != k else 0)

        return max(dp[-1][-1], 0)

