from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 40 ms, faster than 75.51% of Python3 online submissions for Predict the Winner.
Memory Usage: 13.7 MB, less than 5.97% of Python3 online submissions for Predict the Winner.
"""

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * (n) for _ in range(n+1)] 

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j]-dp[i][j-1])
        return dp[0][-1] >= 0
