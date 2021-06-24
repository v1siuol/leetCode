from __future__ import annotations 
import collections 
import random 
import heapq 
import re
import threading


"""
Success
Details 
Runtime: 68 ms, faster than 93.35% of Python3 online submissions for Minimum Time Difference.
Memory Usage: 15.7 MB, less than 100.00% of Python3 online submissions for Minimum Time Difference.
"""
# sort n log n
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        t = sorted(int(time[:2]) * 60 + int(time[3:]) for time in timePoints)
        t.append(1440+t[0])
        return min(b - a for a, b in zip(t, t[1:]))
