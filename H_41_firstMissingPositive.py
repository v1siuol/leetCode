from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 28 ms, faster than 41.62% of Python online submissions for First Missing Positive.
Memory Usage: 11.8 MB, less than 5.31% of Python online submissions for First Missing Positive.
"""

# class Solution(object):
#     def firstMissingPositive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # 看的 diss 

#         # put the right number in the right place 
#         # n = len(nums)

#         # for i in range(n):
#         #     while (0 < nums[i] <= n) and (nums[i] != nums[nums[i]-1]):
#         #         val = nums[i]-1
#         #         nums[i], nums[val] = nums[val], nums[i]

#         # for i in range(n):
#         #     if nums[i] != i+1:
#         #         return i+1

#         # return n+1

#         for i in range(len(nums)):
#             while (0 < nums[i] <= len(nums)) and (nums[i] != nums[nums[i]-1]):
#                 val = nums[i]-1
#                 nums[i], nums[val] = nums[val], nums[i]

#         for i in range(len(nums)):
#             if nums[i] != i+1:
#                 return i+1

#         return len(nums)+1


# s = Solution()

# print(s.firstMissingPositive([]))
# print(s.firstMissingPositive([1]))
# print(s.firstMissingPositive([1,2,0]))
# print(s.firstMissingPositive([3,4,-1,1]))
# print(s.firstMissingPositive([7,8,9,11,12]))



"""
Success
Details 
Runtime: 44 ms, faster than 13.83% of Python3 online submissions for First Missing Positive.
Memory Usage: 14 MB, less than 5.10% of Python3 online submissions for First Missing Positive.
"""

"""
diss 
Put each number in its right place.
For example:
When we find 5, then swap it with A[4].
At last, the first place where its number is not right, return the place + 1.
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[nums[i]-1] != nums[i]:
                t = nums[i]-1
                nums[i], nums[t] = nums[t], nums[i]
        for i, num in enumerate(nums):
            if num != i+1:
                return i+1
        return n+1
