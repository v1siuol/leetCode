from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 44 ms, faster than 75.61% of Python3 online submissions for Arithmetic Slices.
Memory Usage: 14.1 MB, less than 6.93% of Python3 online submissions for Arithmetic Slices.
"""

class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = 0
        count = 0
        for i in range(2, len(A)):
            if A[i-1]-A[i-2] == A[i]-A[i-1]:
                dp += 1
                count += dp
            else:
                dp = 0
        return count 
