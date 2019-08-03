from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 548 ms, faster than 34.25% of Python3 online submissions for 2 Keys Keyboard.
Memory Usage: 13.4 MB, less than 5.77% of Python3 online submissions for 2 Keys Keyboard.
"""

class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(2, n+1):
            dp[i] = i
            for j in range(i-1, 1, -1):
                if i % j == 0:
                    dp[i] = dp[j] + i//j
                    break

        return dp[n]
