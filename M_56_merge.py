from __future__ import annotations 
import collections 
import random 
import heapq 
import math


# """
# Success
# Details 
# Runtime: 104 ms, faster than 5.41% of Python3 online submissions for Merge Intervals.
# Memory Usage: 15.8 MB, less than 11.79% of Python3 online submissions for Merge Intervals.
# """

# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals.sort()
#         res = []
#         for i in intervals:
#             if len(res) == 0 or res[-1][1] < i[0]:
#                 res.append(i)
#             else:
#                 res[-1][1] = max(res[-1][1], i[1])
#         return res 


"""
Success
Details 
Runtime: 92 ms, faster than 97.33% of Python3 online submissions for Merge Intervals.
Memory Usage: 14.6 MB, less than 6.52% of Python3 online submissions for Merge Intervals.
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals.sort()
        res = [intervals[0]]
        for i_start, i_end in intervals[1:]:
            if i_start <= res[-1][-1]:
                res[-1][1] = max(res[-1][1], i_end)
            else:
                res.append([i_start, i_end])

        return res
