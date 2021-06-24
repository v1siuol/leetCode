from __future__ import annotations 
import collections 
import random 
import heapq 
import re
import threading


"""
Success
Details 
Runtime: 76 ms, faster than 92.33% of Python3 online submissions for Minimum Size Subarray Sum.
Memory Usage: 15.3 MB, less than 7.69% of Python3 online submissions for Minimum Size Subarray Sum.
"""
# 双指针 O(n)
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        curr_min = float('inf')
        i = j = 0
        n = len(nums)
        curr_sum = 0
        while j < n:
            curr_sum += nums[j]
            j += 1
            while curr_sum >= s:
                curr_min = min(curr_min, j-i)
                curr_sum -= nums[i]
                i += 1

        return 0 if curr_min == float('inf') else curr_min
