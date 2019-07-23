from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 412 ms, faster than 5.23% of Python3 online submissions for Find All Duplicates in an Array.
Memory Usage: 21.4 MB, less than 5.08% of Python3 online submissions for Find All Duplicates in an Array.
"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # 注意限制解题
        ret = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                ret.append(idx+1)
            else:
                nums[idx] *= -1 
        return ret 

