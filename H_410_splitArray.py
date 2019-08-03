from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 44 ms, faster than 52.94% of Python3 online submissions for Split Array Largest Sum.
Memory Usage: 13.9 MB, less than 5.19% of Python3 online submissions for Split Array Largest Sum.
"""

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        max_num = s = 0
        for num in nums:
            max_num = max(max_num, num)
            s += num
        if max_num == 1:
            return s

        # binary search 
        left = max_num 
        right = s
        while left <= right:
            mid = (left + right) // 2
            if valid(mid, nums, m):
                right = mid - 1
            else:
                left = mid + 1
        return left

def valid(target, nums, m):
    count = 1
    total = 0
    for num in nums:
        total += num
        if total > target:
            total = num
            count += 1
            if count > m:
                return False
    return True 
