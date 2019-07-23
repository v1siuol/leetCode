from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 64 ms, faster than 5.81% of Python3 online submissions for Maximum Product Subarray.
Memory Usage: 14.2 MB, less than 20.06% of Python3 online submissions for Maximum Product Subarray.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        curr_max = curr_min = ret = nums[0]
        for num in nums[1:]:
            if num < 0:
                curr_min, curr_max = curr_max, curr_min
            curr_max = max(num, curr_max*num)
            curr_min = min(num, curr_min*num)
            ret = max(ret, curr_max)
        return ret 


s = Solution()
print(s.maxProduct([2,3,-2,4]))
