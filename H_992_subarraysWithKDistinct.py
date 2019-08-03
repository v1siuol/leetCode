from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 540 ms, faster than 77.78% of Python3 online submissions for Subarrays with K Different Integers.
Memory Usage: 16.2 MB, less than 19.67% of Python3 online submissions for Subarrays with K Different Integers.
"""

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return at_most_k(A, K) - at_most_k(A, K-1)

def at_most_k(nums, K):
    res = 0
    start = 0
    count = 0
    num_count = dict()
    for idx in range(len(nums)):
        if nums[idx] not in num_count:
            # diff kind 
            num_count[nums[idx]] = 1
            count += 1
        else:
            num_count[nums[idx]] += 1

        while count > K:
            num_count[nums[start]] -= 1
            if num_count[nums[start]] == 0:
                count -= 1
                num_count.pop(nums[start])
            start += 1
        res += idx - start + 1

    return res
