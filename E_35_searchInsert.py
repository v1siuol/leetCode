from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
62 / 62 test cases passed.
Status: Accepted
Runtime: 42 ms
You are here!
Your runtime beats 72.83% of python submissions.
"""
# class Solution(object):
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         # binary search
#         low = 0
#         high = len(nums) - 1
#         mid = (low + high) >> 1
#         while True:
#             if target > nums[mid]:
#                 low = mid
#                 mid = (low + high) >> 1
#                 if low == mid:
#                     while low < len(nums) and target > nums[low]:
#                         low += 1
#                     return low
#             elif target < nums[mid]:
#                 high = mid
#                 mid = (low + high) >> 1
#                 if high == mid:
#                     while 0 < high and target < nums[high]:
#                         high -= 1
#                     return high
#             elif target == nums[mid]:
#                 return mid
#         return -1

# print(Solution().searchInsert([1, 3, 5, 6], 5))
# print(Solution().searchInsert([1, 3, 5, 6], 2))
# print(Solution().searchInsert([1, 3, 5, 6], 7))
# print(Solution().searchInsert([1, 3, 5, 6], 0))


"""
Success
Details 
Runtime: 36 ms, faster than 70.17% of Python3 online submissions for Search Insert Position.
Memory Usage: 14.3 MB, less than 5.15% of Python3 online submissions for Search Insert Position.
"""
# 还可以简洁 
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0 
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid 

        return left if nums[left] >= target else left + 1


s = Solution()
print(s.searchInsert([1,3,5,6], 0))
print(s.searchInsert([1,3,5,6], 2))
print(s.searchInsert([1,3,5,6], 5))
print(s.searchInsert([1,3,5,6], 6))
print(s.searchInsert([1,3,5,6], 7))
