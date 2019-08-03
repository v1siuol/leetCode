from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 120 ms, faster than 51.46% of Python3 online submissions for Cheapest Flights Within K Stops.
Memory Usage: 20.2 MB, less than 6.03% of Python3 online submissions for Cheapest Flights Within K Stops.
"""

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        hq = []

        from_to = collections.defaultdict(set)
        for f, to, cost in flights:
            from_to[f].add((to, cost))

        for to, cost in from_to.get(src, []):
            heapq.heappush(hq, (cost, to, 0))

        while hq:
            cost, curr, k = heapq.heappop(hq)
            if curr == dst:
                return cost
            if k + 1 > K:
                continue
            for to, c in from_to.get(curr, []):
                heapq.heappush(hq, (c+cost, to, k+1))


        return -1
