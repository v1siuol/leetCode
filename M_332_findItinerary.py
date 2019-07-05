"""
Success
Details 
Runtime: 60 ms, faster than 71.92% of Python3 online submissions for Reconstruct Itinerary.
Memory Usage: 13.9 MB, less than 10.17% of Python3 online submissions for Reconstruct Itinerary.
"""

from __future__ import annotations 
import collections 
import random 
import heapq 

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = collections.defaultdict(list)
        for a, b in reversed(sorted(tickets)):
            targets[a].append(b)
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]


s = Solution()

print(s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print(s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))