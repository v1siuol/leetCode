from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 64 ms, faster than 36.85% of Python3 online submissions for Jump Game II.
Memory Usage: 14.5 MB, less than 7.50% of Python3 online submissions for Jump Game II.
"""

# class Solution:
#     def jump(self, nums: 'List[int]') -> 'int':
#         if len(nums) == 1:
#             return 0 
#         level = 0
#         current_max = 0
#         loc = 0
#         next_max = 0
#         goal = len(nums) - 1 

#         while current_max >= loc:
#             level += 1
#             while loc <= current_max:
#                 next_max = max(next_max, loc + nums[loc])
#                 if next_max >= goal:
#                     return level
#                 loc += 1
#             current_max = next_max

#         return -1 


# s = Solution()
# print(s.jump([2,3,1,1,4]))
# print(s.jump([0]))
# print(s.jump([2,1]))
# print(s.jump([2,0,2,0,1]))



"""
Success
Details 
Runtime: 124 ms, faster than 6.34% of Python3 online submissions for Jump Game II.
Memory Usage: 15.9 MB, less than 5.47% of Python3 online submissions for Jump Game II.
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0 

        ret = 0
        curr_far = 0 
        curr_end = 0

        for i in range(len(nums)):
            curr_far = max(curr_far, nums[i] + i)

            if curr_far >= len(nums) - 1:
                break

            if i == curr_end:
                ret += 1
                curr_end = curr_far

        return ret + 1 

