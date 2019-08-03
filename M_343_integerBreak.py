from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 24 ms, faster than 100.00% of Python3 online submissions for Integer Break.
Memory Usage: 13.8 MB, less than 5.43% of Python3 online submissions for Integer Break.
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {2:1, 3:2, 4:4, 5:6, 6:9}
        if n <= 6:
            return dp[n]
        left3 = n % 3
        if left3 == 0:
            return 3 ** (n//3)
        elif left3 == 1:
            return 3 ** (n//3-1) * 4
        else:
            return 3 ** (n//3-1) * 6


