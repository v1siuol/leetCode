from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 36 ms, faster than 82.35% of Python3 online submissions for Least Operators to Express Number.
Memory Usage: 13.9 MB, less than 20.00% of Python3 online submissions for Least Operators to Express Number.
"""

class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        # ???????
        pos = neg = k = 0
        while target:
            target, cur = divmod(target, x)
            if k:
                pos, neg = min(cur * k + pos, (cur + 1) * k + neg), min((x - cur) * k + pos, (x - cur - 1) * k + neg)
            else:
                pos, neg = cur * 2, (x - cur) * 2
            k += 1
            # print(target, pos, neg, k)

        return min(pos, k + neg) - 1
