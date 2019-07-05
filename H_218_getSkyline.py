"""
Success
Details 
Runtime: 64 ms, faster than 94.10% of Python3 online submissions for The Skyline Problem.
Memory Usage: 17 MB, less than 65.26% of Python3 online submissions for The Skyline Problem.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 爆难 
        skyline = []
        i, n = 0, len(buildings)
        liveHR = []
        while i < n or liveHR:
            if not liveHR or i < n and buildings[i][0] <= -liveHR[0][1]:
                x = buildings[i][0]
                while i < n and buildings[i][0] == x:
                    heapq.heappush(liveHR, (-buildings[i][2], -buildings[i][1]))
                    i += 1
            else:
                x = -liveHR[0][1]
                while liveHR and -liveHR[0][1] <= x:
                    heapq.heappop(liveHR)
            height = len(liveHR) and -liveHR[0][0]
            if not skyline or height != skyline[-1][1]:
                skyline.append((x, height))
        return skyline


s = Solution()

print(s.getSkyline([ [2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8] ]))
