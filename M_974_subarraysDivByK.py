from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 344 ms, faster than 5.10% of Python3 online submissions for Subarray Sums Divisible by K.
Memory Usage: 17.5 MB, less than 5.23% of Python3 online submissions for Subarray Sums Divisible by K.
"""

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        # pre_sum dict + total O(n)
        m = [0] * K
        m[0] = 1
        count = 0
        s = 0
        for a in A:
            s = (s + a) % K
            if s < 0:
                s += K
            count += m[s]
            m[s] += 1
        return count 

