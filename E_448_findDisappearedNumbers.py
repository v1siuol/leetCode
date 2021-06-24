from __future__ import annotations 
import collections 
import random 
import heapq 


"""
34 / 34 test cases passed.
Status: Accepted
Runtime: 242 ms
You are here!
Your runtime beats 98.68% of python submissions.
"""
# class Solution(object):
#     def findDisappearedNumbers(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         return list(set(list(range(1, len(nums)+1))) - set(nums))

# print(Solution().findDisappearedNumbers([1,1]))


"""
Success
Details 
Runtime: 464 ms, faster than 13.05% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 20.5 MB, less than 46.43% of Python3 online submissions for Find All Numbers Disappeared in an Array.
"""
# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         # O(n) O(1)
#         # for each number, we put them back to original loc 
#         i = 0
#         n = len(nums)
#         while i < n:
            
#             while i != nums[i]-1 and 1 <= nums[i] <= n and nums[i] != nums[nums[i]-1]:
#                 temp = nums[i]-1
#                 nums[i], nums[temp] = nums[temp], nums[i]
#             i += 1
            
#         ret = []
#         for i in range(n):
#             if i+1 != nums[i]:
#                 ret.append(i+1)
                
#         return ret


"""
Success
Details 
Runtime: 396 ms, faster than 77.89% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 20.5 MB, less than 46.43% of Python3 online submissions for Find All Numbers Disappeared in an Array.
"""
# set space换时间 或 in place neg 
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # O(n) O(1)
        for num in nums:
            corr_idx = abs(num)-1
            if nums[corr_idx] > 0:
                nums[corr_idx] *= -1

        ret = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                ret.append(i+1)

        return ret
