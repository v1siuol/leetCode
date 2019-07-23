from __future__ import annotations 
import collections 
import random 
import heapq 
import math

from functools import reduce
from operator import __and__


"""
Success
Details 
Runtime: 68 ms, faster than 14.22% of Python3 online submissions for Permutations.
Memory Usage: 13.4 MB, less than 18.20% of Python3 online submissions for Permutations.
"""

# class Solution:
#     def permute(self, nums: 'List[int]') -> 'List[List[int]]':
#         # ... 优化ma 
#         ret = []

#         backtrack(nums, [], ret, [0] * len(nums))
#         return ret

# def backtrack(nums, path, result, used):
#     if reduce(__and__, used) == 1:
#         result.append(path)
#         return
#     else:
#         for idx, val in enumerate(used):
#             if val == 0:
#                 used[idx] = 1
#                 backtrack(nums, path+[nums[idx]], result, used)
#                 used[idx] = 0

#                 # backtrack(nums, path+[nums[idx]], result, used[:idx]+[1]+used[idx+1:])



# s = Solution()
# print(s.permute([1,2,3]))


"""
Success
Details 
Runtime: 52 ms, faster than 63.28% of Python3 online submissions for Permutations.
Memory Usage: 14 MB, less than 5.19% of Python3 online submissions for Permutations.
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        backtracking(nums, [], ret)
        return ret 

def backtracking(nums, path, ret):
    if not nums:
        ret.append(path)
        return 
    for i in range(len(nums)):
        backtracking(nums[:i]+nums[i+1:], path+[nums[i]], ret)
