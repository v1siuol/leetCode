from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 104 ms, faster than 5.41% of Python3 online submissions for Merge Intervals.
Memory Usage: 15.8 MB, less than 11.79% of Python3 online submissions for Merge Intervals.
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for i in intervals:
            if len(res) == 0 or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        return res 

