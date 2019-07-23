from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 92 ms, faster than 5.66% of Python3 online submissions for Insert Interval.
Memory Usage: 17.2 MB, less than 5.13% of Python3 online submissions for Insert Interval.
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        output.append(newInterval)

        while i < len(intervals):
            output.append(intervals[i])
            i += 1

        return output 

