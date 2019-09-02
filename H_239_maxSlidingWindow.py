from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 180 ms, faster than 71.05% of Python3 online submissions for Sliding Window Maximum.
Memory Usage: 20 MB, less than 15.38% of Python3 online submissions for Sliding Window Maximum.
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        if k == 0:
            return []

        res = []
        deque = collections.deque()
        for idx in range(len(nums)):

            while deque and deque[0] < idx - k + 1:
                # out of bound 
                deque.popleft()

            while deque and nums[deque[-1]] <= nums[idx]:
                # get rid of smaller 
                deque.pop()

            deque.append(idx)
            if idx >= k-1:
                res.append(nums[deque[0]])

        return res
