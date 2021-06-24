from __future__ import annotations 
import collections 
import random 
import heapq 
import math


# TLE 
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         ret = [1] * len(nums)
#         for i in range(len(nums)):
#             for p in range(i):
#                 ret[p] *= nums[i]
#             for q in range(i+1, len(nums)):
#                 ret[q] *= nums[i]
#         return ret 


# """
# Success
# Details 
# Runtime: 132 ms, faster than 6.59% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 20.3 MB, less than 95.47% of Python3 online submissions for Product of Array Except Self.
# """

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         # 左右 list
#         ret = [0] * len(nums)
#         ret[0] = 1
#         for i in range(1, len(nums)):
#             ret[i] = nums[i-1] * ret[i-1]
#         right = 1
#         for i in reversed(range(len(nums))):
#             ret[i] = ret[i] * right
#             right *= nums[i]
#         return ret 


"""
Success
Details 
Runtime: 176 ms, faster than 5.39% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 19.8 MB, less than 96.00% of Python3 online submissions for Product of Array Except Self.
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = collections.deque([1])
        for i in range(1, n):
            left.append(left[-1]*nums[i-1])
        right = collections.deque([1])
        for i in range(n-2, -1, -1):
            right.appendleft(right[0]*nums[i+1])

        return [left[i]*right[i] for i in range(n)]
