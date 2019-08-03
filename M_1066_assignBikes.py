from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 124 ms, faster than 82.72% of Python3 online submissions for Campus Bikes II.
Memory Usage: 14.4 MB, less than 25.00% of Python3 online submissions for Campus Bikes II.
"""

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def dis(i, j):
            return abs(workers[i][0]-bikes[j][0]) + abs(workers[i][1]-bikes[j][1])
        h = [[0,0,0]]
        seen = set()
        while True:
            cost, i, taken = heapq.heappop(h)
            if (i, taken) in seen:
                continue
            seen.add((i, taken))
            if i == len(workers):
                return cost
            for j in range(len(bikes)):
                if taken & (1 << j) == 0:
                    heapq.heappush(h, [cost+dis(i,j), i+1, taken | (1 << j)])


s = Solution()
workers = [[815,60],[638,626],[6,44],[103,90],[591,880]]
bikes = [[709,161],[341,339],[755,955],[172,27],[433,489]]
print(s.assignBikes(workers, bikes))
