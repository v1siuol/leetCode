from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect




class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        ret1 = 0

        nums1 = nums[:]
        for i in range(1, len(nums1), 2):
            at_least = float('inf')
            if i - 1 >= 0:
                at_least = nums1[i-1] - 1
            if i + 1 < len(nums1):
                at_least = min(at_least, nums1[i+1]-1)
            if nums1[i] > at_least:
                ret1 += nums1[i] - at_least
                nums1[i] = at_least

        # t2
        ret2 = 0
        for i in range(0, len(nums), 2):
            at_least = float('inf')
            if i - 1 >= 0:
                at_least = nums[i-1] - 1
            if i + 1 < len(nums):
                at_least = min(at_least, nums[i+1]-1)
            if nums[i] > at_least:
                ret2 += nums[i] - at_least
                nums[i] = at_least

        return min(ret1, ret2)



s = Solution()

nums = [1,2,3]  # 2
print(s.movesToMakeZigzag(nums))

nums = [9,6,1,6,2]  # 4
print(s.movesToMakeZigzag(nums))
