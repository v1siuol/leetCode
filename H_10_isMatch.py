from __future__ import annotations 
import collections 
import random 
import heapq 
import math

"""
Success
Details 
Runtime: 56 ms, faster than 73.54% of Python3 online submissions for Regular Expression Matching.
Memory Usage: 13.4 MB, less than 24.64% of Python3 online submissions for Regular Expression Matching.
"""

class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        # nan 

        dp = [[False] * (len(p) + 1) for _ in range(len(s)+1)]
        dp[0][0] = True 
        
        for i, char in enumerate(p):
            if char == '*' and dp[0][i-1]:
                dp[0][i+1] = True 

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == '.':
                    dp[i+1][j+1] = dp[i][j]
                if p[j] == s[i]:
                    dp[i+1][j+1] = dp[i][j]
                if p[j] == '*':
                    if p[j-1] != s[i] and p[j-1] != '.':
                        dp[i+1][j+1] = dp[i+1][j-1]
                    else:
                        dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1] or dp[i+1][j-1]

        # return dp[len(s)][len(p)]
        return dp[-1][-1]
