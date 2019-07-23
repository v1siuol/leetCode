from __future__ import annotations 
import collections 
import random 
import heapq 
import math

"""
Success
Details 
Runtime: 72 ms, faster than 5.52% of Python3 online submissions for Maximum Subarray.
Memory Usage: 14.6 MB, less than 5.07% of Python3 online submissions for Maximum Subarray.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            max_sum = max(max_sum, nums[i])
        return max_sum


"""
Success
Details 
Runtime: 88 ms, faster than 5.04% of Python3 online submissions for Maximum Subarray.
Memory Usage: 14.5 MB, less than 5.07% of Python3 online submissions for Maximum Subarray.
"""

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         curr_sum = 0
#         max_sum = nums[0]
#         for num in nums:
#             curr_sum += num
#             max_sum = max(max_sum, curr_sum)
#             if curr_sum < 0:
#                 curr_sum = 0
#         return max_sum
