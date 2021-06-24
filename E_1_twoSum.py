from __future__ import annotations 
import collections 
import random 
import heapq 

"""
Success
Details 
Runtime: 32 ms, faster than 96.82% of Python3 online submissions for Two Sum.
Memory Usage: 14.7 MB, less than 17.04% of Python3 online submissions for Two Sum.
"""


"""
缓存差值字典
29 / 29 test cases passed.
Status: Accepted
Runtime: 32 ms
You are here! 
Your runtime beats 57.58 % of python submissions.
"""

# class Solution:
#     def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
#         # Times: O(n)
#         # Space: O(n)

#         dct = dict()

#         for idx, num in enumerate(nums):
#             if num in dct:
#                 return [dct[num], idx]
#             dct[target-num] = idx


"""
Success
Details 
Runtime: 60 ms, faster than 68.79% of Python3 online submissions for Two Sum.
Memory Usage: 15.1 MB, less than 5.58% of Python3 online submissions for Two Sum.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time O(n) one pass Space O(n) store N key/value 
        look_up_dict = dict()  # store the to-match num: idx
        
        for idx, num in enumerate(nums):  # loop 
            if num in look_up_dict:
                return [look_up_dict[num], idx]  # found 
            look_up_dict[target-num] = idx  # store

