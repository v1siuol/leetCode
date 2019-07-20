from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 36 ms, faster than 91.75% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 13.8 MB, less than 79.29% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
"""

# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         # 边界神仙  
#         res = [-1, -1]

#         if not nums:
#             return res

#         left = 0
#         right = len(nums) - 1

#         while left < right:
#             mid = (left + right) // 2
#             if nums[mid] < target:
#                 left = mid + 1 
#             else:
#                 right = mid 

#         if nums[left] != target:
#             return res
#         else:
#             res[0] = left

#         right = len(nums) - 1
#         while left < right:
#             mid = (left + right) // 2 + 1
#             if nums[mid] <= target:
#                 left = mid
#             else:
#                 right = mid - 1 

#         res[1] = right
#         return res



# s = Solution()

# nums = [5,7,7,8,8,10]
# target = 8
# print(s.searchRange(nums, target))  # [3,4]

# nums = [5,7,7,8,8,10]
# target = 6
# print(s.searchRange(nums, target))  # [-1,-1]

# nums = [5,7,7,7,8,10]
# target = 8
# print(s.searchRange(nums, target))  # [4,4]

# nums = []
# target = 0
# print(s.searchRange(nums, target))  # [-1,-1]



"""
Success
Details 
Runtime: 52 ms, faster than 10.85% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 14.7 MB, less than 5.57% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        left = 0
        right = len(nums) - 1 
        ret = [-1,-1]

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid 

        if nums[left] != target:
            return ret 
        else:
            ret[0] = left 

        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid 

        ret[1] = right 

        return ret 
