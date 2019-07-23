from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 32 ms, faster than 93.22% of Python3 online submissions for Sort Colors.
Memory Usage: 13.9 MB, less than 5.23% of Python3 online submissions for Sort Colors.
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 2ptr swap dutch national flag problem 
        second = len(nums) - 1
        zero = 0
        curr = 0

        while curr <= second:
            if nums[curr] == 2:
                nums[curr], nums[second] = nums[second], nums[curr]
                second -= 1
            elif nums[curr] == 0:
                nums[curr], nums[zero] = nums[zero], nums[curr]
                zero += 1
                curr += 1
            else:
                curr += 1
