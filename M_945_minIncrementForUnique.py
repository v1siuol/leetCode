from __future__ import annotations 
import collections 
import random 
import heapq 


"""
Success
Details 
Runtime: 556 ms, faster than 18.07% of Python3 online submissions for Minimum Increment to Make Array Unique.
Memory Usage: 31.7 MB, less than 50.00% of Python3 online submissions for Minimum Increment to Make Array Unique.
"""
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        # union find O(n) dont know 
        root = {}
        def find(x):
            if x not in root:
                root[x] = x
            elif x != root[x]:
                root[x] = find(root[x])
            elif x + 1 in root:
                root[x] = find(root[x + 1])
            else:
                root[x] = root[x + 1] = x + 1
            return root[x]
        return sum(find(a) - a for a in A)
