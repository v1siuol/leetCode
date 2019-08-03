from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 48 ms, faster than 87.01% of Python3 online submissions for Minimum Cost For Tickets.
Memory Usage: 13.9 MB, less than 11.33% of Python3 online submissions for Minimum Cost For Tickets.
"""

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cost = 0
        q7 = collections.deque()
        q30 = collections.deque()

        for day in days:
            while q7 and q7[0][0] + 7 <= day:
                q7.popleft()
            while q30 and q30[0][0] + 30 <= day:
                q30.popleft()
            q7.append((day, cost+costs[1]))
            q30.append((day, cost+costs[2]))
            cost = min(cost+costs[0], q7[0][1], q30[0][1])
        return cost 
