from __future__ import annotations 
import collections 
import random 
import heapq 
import re
import threading


"""
uccess
Details 
Runtime: 164 ms, faster than 86.96% of Python3 online submissions for Find Pivot Index.
Memory Usage: 14 MB, less than 75.00% of Python3 online submissions for Find Pivot Index.
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        curr = 0
        for i in range(len(nums)):
            if curr == total_sum - nums[i]:
                return i
            curr += nums[i]
            total_sum -= nums[i]
        return -1
