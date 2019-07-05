"""
Success
Details 
Runtime: 48 ms, faster than 92.65% of Python3 online submissions for Number of Connected Components in an Undirected Graph.
Memory Usage: 14.3 MB, less than 62.67% of Python3 online submissions for Number of Connected Components in an Undirected Graph.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        roots = [i for i in range(n)]

        for e in edges:
            r1 = find(roots, e[0])
            r2 = find(roots, e[1])
            if r1 != r2:
                roots[r1] = r2  # union  
                n -= 1
        return n 

def find(roots, id):
    while roots[id] != id:
        roots[id] = roots[roots[id]]
        id = roots[id]
    return id


s = Solution()

n = 5
edges = [[0, 1], [1, 2], [3, 4]]
res = s.countComponents(n, edges)
exp = 2
print(res, res == exp)

n = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
res = s.countComponents(n, edges)
exp = 1
print(res, res == exp)
