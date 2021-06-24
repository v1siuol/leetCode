from __future__ import annotations 
import collections 
import random 
import heapq 
import re


"""
Success
Details 
Runtime: 324 ms, faster than 92.12% of Python3 online submissions for Minimum Cost to Connect Sticks.
Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Minimum Cost to Connect Sticks.
"""
# greedy 
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            c = heapq.heappop(sticks) + heapq.heappop(sticks)
            cost += c
            heapq.heappush(sticks, c)

        return cost
