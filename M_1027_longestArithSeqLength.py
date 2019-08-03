from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 1424 ms, faster than 61.19% of Python3 online submissions for Longest Arithmetic Sequence.
Memory Usage: 372 MB, less than 13.99% of Python3 online submissions for Longest Arithmetic Sequence.
"""

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = dict()
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                dp[(j, A[j]-A[i])] = dp.get((i, A[j]-A[i]), 1) + 1
        return max(dp.values())

