from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
113 / 113 test cases passed.
Status: Accepted
Runtime: 42 ms
You are here!
Your runtime beats 78.69 % of python submissions.
"""
# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         i = 0
#         res = len(nums)
#         while i < len(nums):
#             if val == nums[i]:
#                 nums.pop(i)
#                 res -= 1
#             else:
#                 i += 1
#         return res

# print(Solution().removeElement([3,2,2,3], 3))


"""
Success
Details 
Runtime: 36 ms, faster than 76.01% of Python3 online submissions for Remove Element.
Memory Usage: 13.3 MB, less than 5.91% of Python3 online submissions for Remove Element.
"""
# sol 还有一手移花接木 
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i 
