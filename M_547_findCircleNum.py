from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 216 ms, faster than 87.70% of Python3 online submissions for Friend Circles.
Memory Usage: 13.9 MB, less than 35.29% of Python3 online submissions for Friend Circles.
"""

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # union find 
        n = len(M)
        count = n
        roots = [i for i in range(n)]
        for i in range(n-1):
            for j in range(i+1, n):
                # upper right matrix / not include diagonals 
                if M[i][j] == 1:
                    x = find(roots, i)
                    y = find(roots, j)
                    if x != y:
                        roots[x] = y
                        count -=1

        return count

def find(roots, id):
    while roots[id] != id:
        roots[id] = roots[roots[id]]
        id = roots[id]
    return id
