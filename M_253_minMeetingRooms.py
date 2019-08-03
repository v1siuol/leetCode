from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 88 ms, faster than 86.81% of Python3 online submissions for Meeting Rooms II.
Memory Usage: 17.2 MB, less than 5.41% of Python3 online submissions for Meeting Rooms II.
"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        start, end = zip(*intervals)

        start = sorted(start)
        end = sorted(end)

        rooms = 0
        end_idx = 0
        for s in start:
            if s < end[end_idx]:
                rooms += 1
            else:
                end_idx += 1
        return rooms
