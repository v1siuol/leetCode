from __future__ import annotations 
import collections 
import random 
import heapq 
import math

"""
Success
Details 
Runtime: 1224 ms, faster than 98.50% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
"""

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        if A[0] == B[0]:
            val = [A[0]]
        else:
            val = [A[0], B[0]]

        a_to = collections.defaultdict(int)
        b_to = collections.defaultdict(int)

        for i in range(len(A)):
            j = 0
            while j < len(val):
                if val[j] == A[i]:
                    if val[j] != B[i]:
                        b_to[val[j]] += 1
                    j += 1
                elif val[j] == B[i]:
                    if val[j] != A[i]:
                        a_to[val[j]] += 1
                    j += 1
                else:
                    v = val.pop(j)
                    if v in a_to:
                        a_to.pop(v)
                    if v in b_to:
                        b_to.pop(v)
                    if len(val) == 0:
                        return -1
        if len(val) == 2:
            return a_to[val[0]]
        else:
            return min(a_to[val[0]], b_to[val[0]])
