from __future__ import annotations 
import collections 
import random 
import heapq 
import re
import threading


"""
Success
Details 
Runtime: 880 ms, faster than 89.39% of Python3 online submissions for Shortest Subarray with Sum at Least K.
Memory Usage: 19.6 MB, less than 25.00% of Python3 online submissions for Shortest Subarray with Sum at Least K.
"""
# 魔法queue O(n)
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        queue = collections.deque([[0,0]])

        res = float('inf')
        s = 0

        for i, val in enumerate(A):
            s += val

            while queue and s - queue[0][1] >= K:
                res = min(res, i+1-queue.popleft()[0])

            while queue and s <= queue[-1][1]:
                queue.pop()

            queue.append([i+1, s])

        return -1 if res == float('inf') else res
