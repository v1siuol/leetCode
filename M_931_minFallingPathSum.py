from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 152 ms, faster than 18.29% of Python3 online submissions for Minimum Falling Path Sum.
Memory Usage: 14.5 MB, less than 14.28% of Python3 online submissions for Minimum Falling Path Sum.
"""

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        dp = A[0]

        for row in A[1:]:
            prev = dp[:]
            for i in range(len(row)):
                if i == 0:
                    dp[i] = min(prev[i:i+2]) + row[i]
                elif i == len(row)-1:
                    dp[i] = min(prev[i-1:i+1]) + row[i]
                else:
                    dp[i] = min(prev[i-1:i+2]) + row[i]

        return min(dp)
