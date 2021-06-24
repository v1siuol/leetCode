from __future__ import annotations 
import collections 
import random 
import heapq 
import re
import threading


"""
Success
Details 
Runtime: 136 ms, faster than 40.55% of Python3 online submissions for Super Egg Drop.
Memory Usage: 19.6 MB, less than 11.11% of Python3 online submissions for Super Egg Drop.
"""
# 恐怖
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [ [0] * (K+1) for _ in range(N+1) ]
        for m in range(1, N+1):
            for k in range(1, K+1):
                dp[m][k] = 1 + dp[m-1][k-1] + dp[m-1][k]
            if dp[m][K] >= N:
                return m
