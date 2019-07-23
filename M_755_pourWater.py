from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 88 ms, faster than 55.52% of Python3 online submissions for Pour Water.
Memory Usage: 13.9 MB, less than 5.36% of Python3 online submissions for Pour Water.
"""

class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        for _ in range(V):
            curr = K
            while curr > 0 and heights[curr-1] <= heights[curr]:
                curr -= 1

            while curr < len(heights)-1 and heights[curr] >= heights[curr+1]:
                curr += 1

            while K < curr and heights[curr-1] == heights[curr]:
                curr -= 1

            heights[curr] += 1

        return heights

