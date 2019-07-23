from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 272 ms, faster than 5.08% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 15.6 MB, less than 5.20% of Python3 online submissions for Squares of a Sorted Array.
"""

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        right = 0
        for i in range(len(A)):
            if A[i] >= 0:
                right = i
                break

        if i == 0:
            return [a * a for a in A]

        left = right - 1
        # -2 -1    0      1 2
        #    left  right 

        ret = []
        while left >= 0 and right < len(A):
            if abs(A[left]) > A[right]:
                ret.append(A[right] * A[right])
                right += 1
            else:
                ret.append(A[left] * A[left])
                left -= 1

        while left >= 0:
            ret.append(A[left] * A[left])
            left -= 1

        while right < len(A):
            ret.append(A[right] * A[right])
            right += 1

        return ret 
