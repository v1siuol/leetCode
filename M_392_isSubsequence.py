from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 292 ms, faster than 8.24% of Python3 online submissions for Is Subsequence.
Memory Usage: 18.4 MB, less than 14.03% of Python3 online submissions for Is Subsequence.
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True 
        s_idx = 0
        t_idx = 0
        while t_idx < len(t):
            if s[s_idx] == t[t_idx]:
                s_idx += 1
            if s_idx == len(s):
                return True 
            t_idx += 1
        return False

