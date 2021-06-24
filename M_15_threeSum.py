from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 1068 ms, faster than 38.46% of Python3 online submissions for 3Sum.
Memory Usage: 16.7 MB, less than 82.74% of Python3 online submissions for 3Sum.
"""

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         ret = []
#         n = len(nums)

#         nums.sort()
#         for i in range(n-2):
#             if i == 0 or (i > 0 and nums[i] != nums[i-1]):
#                 lo = i + 1
#                 hi = n-1
#                 target = -nums[i]

#                 while lo < hi:
#                     if nums[lo] + nums[hi] == target:
#                         ret.append([nums[i], nums[lo], nums[hi]])
#                         while lo < hi and nums[lo] == nums[lo+1]:
#                             lo += 1
#                         while lo < hi and nums[hi] == nums[hi-1]:
#                             hi -= 1 
#                         lo += 1
#                         hi -= 1
#                     elif nums[lo] + nums[hi] < target:
#                         lo += 1
#                     else:
#                         hi -= 1


#         return ret 


"""
Success
Details 
Runtime: 1012 ms, faster than 48.42% of Python3 online submissions for 3Sum.
Memory Usage: 17.1 MB, less than 25.00% of Python3 online submissions for 3Sum.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # backtracking 
        # O(n^2)?
        res = []
        nums.sort()
        backtracking(nums, 0, [], res, 3, 0)
        return res

def backtracking(nums, target, path, res, k, start_idx):
    if k == 2:
        i = start_idx
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                res.append(path+[nums[i], nums[j]])
                while i < j and nums[i] == nums[i+1]:
                    i += 1
                while i < j and nums[j] == nums[j-1]:
                    j -= 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
    else:
        for i in range(start_idx, len(nums)):
            new_path = nums[i]
            new_target = target - nums[i]
            if i > start_idx and nums[i] == nums[i-1]:
                continue
            backtracking(nums, new_target, path+[new_path], res, k-1, i+1)
