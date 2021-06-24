from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 28 ms, faster than 99.43% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 13.1 MB, less than 90.71% of Python3 online submissions for Search in Rotated Sorted Array.
"""

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         # find rotation index 
#         n = len(nums)

#         if n == 0:
#             return -1 
#         if n == 1:
#             return 0 if nums[0] == target else -1 

#         left = 0
#         right = n - 1

#         ror = find_smallest(nums, left, right)

#         if target == nums[ror]:
#             return ror 

#         if ror != 0:
#             if target > nums[0]:
#                 right = ror - 1
#             elif target < nums[0]:
#                 left = ror + 1
#             else:
#                 return 0 

#         while left <= right:
#             mid = left + (right - left) // 2
#             if target < nums[mid]:
#                 right = mid - 1
#             elif target > nums[mid]:
#                 left = mid + 1
#             else:
#                 return mid

#         return -1


# def find_smallest(nums, left, right):
#     if nums[left] < nums[right]:
#         return 0

#     while left <= right:
#         mid = left + (right - left) // 2
#         if nums[mid] > nums[mid+1]:
#             return mid+1
#         else:
#             if nums[mid] < nums[left]:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#     return 0 



# s = Solution()

# nums = [4,5,6,7,0,1,2]
# target = 0
# print(s.search(nums, target))  # 4 


# nums = [4,5,6,7,0,1,2]
# target = 3
# print(s.search(nums, target))  # -1 


# nums = [4,5,6,7,0,1,2]
# assert find_smallest(nums, 0, len(nums)-1) == 4
# nums = [4,5,0,1,2]
# assert find_smallest(nums, 0, len(nums)-1) == 2


# nums = [1,3]
# target = 3
# print(s.search(nums, target))  # 1 

# nums = [5,1,3]
# target = 3
# print(s.search(nums, target))  # 2 



# nums = [5,1,3]
# target = 5
# print(s.search(nums, target))  # 0


"""
Success
Details 
Runtime: 32 ms, faster than 91.17% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.1 MB, less than 5.22% of Python3 online submissions for Search in Rotated Sorted Array.
"""

# binary search 
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         if n == 0:
#             return -1 
#         if n == 1:
#             return 0 if nums[0] == target else -1 

#         pivot = find_pivot(nums)

#         left = 0
#         right = len(nums) - 1 
#         if pivot != 0:
#             if nums[0] <= target:
#                 right = pivot - 1
#             else:
#                 left = pivot

#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] < target:
#                 left = mid + 1
#             elif nums[mid] > target:
#                 right = mid - 1
#             else:
#                 return mid

#         return -1 

# # find pivot 
# def find_pivot(nums):
#     left = 0
#     right = len(nums)-1
#     if nums[left] < nums[right]:
#         return 0 

#     while left <= right:
#         mid = (left + right) // 2 
#         if nums[mid] > nums[mid+1]:
#             return mid+1
#         else:
#             if nums[left] > nums[mid]:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#     return None 


"""
Success
Details 
Runtime: 40 ms, faster than 98.26% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Search in Rotated Sorted Array.
"""
# 先找点再找值
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:

#         if len(nums) == 0:
#             return -1
#         if len(nums) == 1:
#             return 0 if nums[0] == target else -1

#         pivot = 0

#         if nums[0] > nums[-1]:
#             i = 0
#             j = len(nums)-1

#             while i <= j:
#                 mid = (i + j) // 2

#                 if nums[mid] > nums[mid+1]:
#                     pivot = mid + 1
#                     break
#                 else:
#                     if nums[i] > nums[mid]:
#                         j = mid - 1
#                     else:
#                         i = mid + 1
#         # pivot find 
#         if pivot == 0:
#             return binsearch(nums, 0, len(nums)-1, target)
#         if target == nums[0]:
#             return 0
#         elif target > nums[0]:
#             return binsearch(nums, 0, pivot-1, target)
#         else:
#             return binsearch(nums, pivot, len(nums)-1, target)

# def binsearch(nums, i, j, target):
#     while i <= j:
#         mid = (i + j) // 2
#         if target == nums[mid]:
#             return mid
#         elif target < nums[mid]:
#             j = mid - 1
#         else:
#             i = mid + 1
#     return -1


"""
Success
Details 
Runtime: 40 ms, faster than 63.76% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Search in Rotated Sorted Array.
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if target == nums[0] else -1

        if nums[0] < nums[-1]:
            return binary_search(nums, 0, n-1, target)
        else:
            p = find_pivot(nums, 0, n-1)
            if target == nums[0]:
                return 0
            elif target < nums[0]:
                return binary_search(nums, p, n-1, target)
            else:
                return binary_search(nums, 0, p-1, target)

# smallest 
def find_pivot(nums, left, right):
    while left <= right:  # 
        mid = (left + right) // 2
        if nums[mid] > nums[mid+1]:
            return mid + 1
        else:
            if nums[left] > nums[mid]:  # 
                right = mid - 1
            else:
                left = mid + 1
    return left

def binary_search(nums, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 
