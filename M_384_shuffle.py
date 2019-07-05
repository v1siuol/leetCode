"""
Success
Details 
Runtime: 464 ms, faster than 61.86% of Python3 online submissions for Shuffle an Array.
Memory Usage: 19.1 MB, less than 71.81% of Python3 online submissions for Shuffle an Array.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.ori = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.ori[:]
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.nums)):
            swap_idx = random.randrange(i, len(self.nums))
            self.nums[i], self.nums[swap_idx] = self.nums[swap_idx], self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()