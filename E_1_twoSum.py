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


class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        # Times: O(n)
        # Space: O(n)

        dct = dict()

        for idx, num in enumerate(nums):
            if num in dct:
                return [dct[num], idx]
            dct[target-num] = idx
