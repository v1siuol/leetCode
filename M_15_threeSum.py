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

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        n = len(nums)

        nums.sort()
        for i in range(n-2):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                lo = i + 1
                hi = n-1
                target = -nums[i]

                while lo < hi:
                    if nums[lo] + nums[hi] == target:
                        ret.append([nums[i], nums[lo], nums[hi]])
                        while lo < hi and nums[lo] == nums[lo+1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi-1]:
                            hi -= 1 
                        lo += 1
                        hi -= 1
                    elif nums[lo] + nums[hi] < target:
                        lo += 1
                    else:
                        hi -= 1


        return ret 


