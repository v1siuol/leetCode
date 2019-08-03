from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 768 ms, faster than 55.56% of Python3 online submissions for Minimum ASCII Delete Sum for Two Strings.
Memory Usage: 18.4 MB, less than 12.50% of Python3 online submissions for Minimum ASCII Delete Sum for Two Strings.
"""

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        # base 
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+ord(s1[i-1]), dp[i][j-1]+ord(s2[j-1]))

        return dp[m][n]
