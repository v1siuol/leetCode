from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 36 ms, faster than 70.90% of Python3 online submissions for Unique Binary Search Trees.
Memory Usage: 13.9 MB, less than 5.76% of Python3 online submissions for Unique Binary Search Trees.
"""

class Solution:
    def numTrees(self, n: int) -> int:
        c = 1
        for i in range(n):
            c = c * (4 * i + 2) // (i + 2)
        return c
