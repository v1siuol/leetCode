from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 136 ms, faster than 5.38% of Python3 online submissions for Subarray Sum Equals K.
Memory Usage: 17.8 MB, less than 5.12% of Python3 online submissions for Subarray Sum Equals K.
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        res = 0
        s = 0
        pre_sum = collections.defaultdict(int)
        pre_sum[0] = 1 
        for num in nums:
            s += num
            if pre_sum[s-k] > 0:
                res += pre_sum[s-k]
            pre_sum[s] += 1
        return res 
