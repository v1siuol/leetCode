"""
Success
Details 
Runtime: 32 ms, faster than 99.04% of Python3 online submissions for Graph Valid Tree.
Memory Usage: 14.4 MB, less than 51.06% of Python3 online submissions for Graph Valid Tree.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nums = [-1] * n
        if n-1 != len(edges):
            return False 

        # union find 
        for i, j in edges:
            x = find(nums, i)
            y = find(nums, j)
            if x == y:
                return False
            nums[x] = y 

        return True 


def find(nums, i):
    if nums[i] == -1:
        return i 
    return find(nums, nums[i])


s = Solution()

n = 5
edges = [[0,1], [0,2], [0,3], [1,4]]
res = s.validTree(n, edges)
exp = True
print(res, res == exp)

n = 5
edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
res = s.validTree(n, edges)
exp = False
print(res, res == exp)
