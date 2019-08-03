from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 796 ms, faster than 34.19% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 19.3 MB, less than 5.18% of Python3 online submissions for K Closest Points to Origin.
"""

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # O(NlogK)
        max_heap = []

        for point in points:
            heapq.heappush(max_heap, (-dis(point), point))
            if len(max_heap) > K:
                heapq.heappop(max_heap)

        ret = [None] * K
        for i in range(K)[::-1]:
            ret[i] = heapq.heappop(max_heap)[1]
        return ret

def dis(p1):
    return p1[0] ** 2 + p1[1] ** 2 
