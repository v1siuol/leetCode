from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 320 ms, faster than 78.87% of Python3 online submissions for Knight Dialer.
Memory Usage: 13.8 MB, less than 29.73% of Python3 online submissions for Knight Dialer.
"""

class Solution:
    def knightDialer(self, N: int) -> int:
        x0 = x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = 1
        for _ in range(N-1):
            x0, x1, x2, x3, x4, x5, x6, x7, x8, x9 = \
                x4+x6, x6+x8, x7+x9, x4+x8, x0+x3+x9, \
                0, x0+x1+x7, x2+x6, x1+x3, x2+x4
        return (x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9) % (10**9 + 7)
