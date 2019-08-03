from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 40 ms, faster than 54.55% of Python3 online submissions for 4 Keys Keyboard.
Memory Usage: 13.7 MB, less than 10.00% of Python3 online submissions for 4 Keys Keyboard.
"""

class Solution:
    def maxA(self, N: int) -> int:
        ret = list(range(N+1))
        for i in range(7, N+1):
            ret[i] = max(ret[i-3]*2, ret[i-4]*3, ret[i-5]*4)
        return ret[N]

