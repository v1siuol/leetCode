"""
Success
Details 
Runtime: 84 ms, faster than 82.89% of Python3 online submissions for Minimum Height Trees.
Memory Usage: 17.7 MB, less than 61.05% of Python3 online submissions for Minimum Height Trees.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = [set() for _ in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        leaves = [i for i in range(n) if len(adj[i]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for l in leaves:
                j = adj[l].pop()
                adj[j].remove(l)
                if len(adj[j]) == 1:
                    new_leaves.append(j)
            leaves = new_leaves
        return leaves


s = Solution()

n = 4
edges = [[1, 0], [1, 2], [1, 3]]
res = s.findMinHeightTrees(n, edges)
exp = [1]
print(res, res == exp)

n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
res = s.findMinHeightTrees(n, edges)
exp = [3,4]
print(res, res == exp)
