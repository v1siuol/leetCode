from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 244 ms, faster than 70.89% of Python3 online submissions for Maximum Length of Pair Chain.
Memory Usage: 14.1 MB, less than 5.00% of Python3 online submissions for Maximum Length of Pair Chain.
"""

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur = float('-inf')
        res = 0
        for a, b in sorted(pairs, key=lambda x: x[1]):
            if cur < a:
                cur = b
                res += 1
        return res 
