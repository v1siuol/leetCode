from __future__ import annotations 
import collections 
import random 
import heapq 
import math

# """
# Runtime: 1580 ms, faster than 11.96% of Python3 online submissions for 4Sum.
# reduce to 2sum, care repetition  
# """

# class Solution:
#     def fourSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         nums.sort()
#         return self.k_sum(nums, target, 4)


#     def k_sum(self, nums, target, k):
#         ret_lst = []

#         if k == 2:
#             left_index = 0      
#             right_index = len(nums) - 1
#             while left_index < right_index: 
#                 if nums[left_index]+nums[right_index] < target:
#                     while left_index < right_index and nums[left_index] == nums[left_index+1]:
#                         left_index += 1
#                     left_index += 1
#                 elif nums[left_index]+nums[right_index] > target:
#                     while left_index < right_index and nums[right_index] == nums[right_index-1]:
#                         right_index -= 1
#                     right_index -= 1
#                 else: 
#                     ret_lst.append([nums[left_index], nums[right_index]])
#                     while left_index < right_index and nums[left_index] == nums[left_index+1]:
#                         left_index += 1
#                     while left_index < right_index and nums[right_index] == nums[right_index-1]:
#                         right_index -= 1
#                     left_index += 1
#                     right_index -= 1
#         else:
#             fix_index = 0
#             while fix_index < len(nums)-k+1:
#                 from_lower_layer = self.k_sum(nums[fix_index+1:], target-nums[fix_index], k-1)
#                 for one_pos in from_lower_layer:
#                     ret_lst.append([nums[fix_index]] + one_pos)

#                 while fix_index + 1 < len(nums) and nums[fix_index] == nums[fix_index+1]:
#                     fix_index += 1

#                 fix_index += 1

#         return ret_lst


# sol = Solution()
# # ret = sol.fourSum([1, 0, -1, 0, -2, 2], 0)
# ret = sol.fourSum([-3,-2,-1,0,0,1,1,1,2,2], 0)
# print(ret)
# print(len(ret))  # 7


"""
Success
Details 
Runtime: 100 ms, faster than 85.11% of Python3 online submissions for 4Sum.
Memory Usage: 13.2 MB, less than 80.52% of Python3 online submissions for 4Sum.
"""

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()
        k_sum(nums, 0, len(nums)-1, target, [], ret, 4)
        return ret 


def k_sum(nums, left, right, target, path, ret, n):
    if right-left+1 < n or n < 2 or target < nums[left]*n or target > nums[right]*n:
        return 
    if n == 2:
        while left < right:
            s = nums[left] + nums[right]
            if s < target:
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                left += 1
            elif s > target:
                while left < right and nums[right] == nums[right-1]:
                    right -= 1 
                right -= 1
            else:
                ret.append(path+[nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1 
                left += 1
                right -= 1
    else:
        for i in range(left, right+1):
            if i == left or nums[i-1] != nums[i]:
                k_sum(nums, i+1, right, target-nums[i], path+[nums[i]], ret, n-1)
