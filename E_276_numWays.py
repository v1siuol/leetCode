from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 32 ms, faster than 87.50% of Python3 online submissions for Paint Fence.
Memory Usage: 13.9 MB, less than 12.20% of Python3 online submissions for Paint Fence.
"""

class Solution:
    def numWays(self, n: int, k: int) -> int:
        # 每个之后都可以涂不同 且不同有k-1种 / 之后同的是因为之前不同 所以之前的diff 
        if n == 0:
            return 0
        if n == 1:
            return k
        diff_color_count = k * (k-1)
        same_color_count = k
        for _ in range(2, n):
            temp = diff_color_count
            diff_color_count = (diff_color_count + same_color_count) * (k-1)
            same_color_count = temp
        return diff_color_count + same_color_count
