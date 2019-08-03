from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 168 ms, faster than 58.72% of Python3 online submissions for Longest String Chain.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Longest String Chain.
"""

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = dict()
        for word in sorted(words, key=len):
            dp[word] = max(dp.get(word[:i]+word[i+1:], 0)+1 for i in range(len(word)))
        return max(dp.values())
