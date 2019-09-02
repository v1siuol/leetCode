from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 280 ms, faster than 57.94% of Python3 online submissions for Employee Free Time.
Memory Usage: 17.5 MB, less than 25.00% of Python3 online submissions for Employee Free Time.
"""

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def employeeFreeTime(self, schedule: 'list<list<Interval>>') -> 'list<Interval>':
        pq = []
        res = []

        for intervals in schedule:
            for interval in intervals:
                heapq.heappush(pq, (interval.start, interval.end))

        temp = heapq.heappop(pq)
        while pq:
            if temp[1] < pq[0][0]:
                # no intersection
                res.append(Interval(temp[1], pq[0][0]))
                temp = heapq.heappop(pq)
            else:
                if temp[1] < pq[0][1]:
                    # extend
                    temp = pq[0]
                heapq.heappop(pq)

        return res 
