"""
Success
Details 
Runtime: 216 ms, faster than 99.26% of Python3 online submissions for Number of Islands II.
Memory Usage: 16.3 MB, less than 88.74% of Python3 online submissions for Number of Islands II.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # dirs = [0, 1, 0, -1, 0]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = []

        count = 0 
        roots = [-1] * (m*n)
        for x,y in positions:
            root = n * x + y
            if roots[root] == -1:
                roots[root] = root
                count += 1 

                for dx, dy in dirs:
                    new_x = x + dx
                    new_y = y + dy
                    new_root = n * new_x + new_y

                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or roots[new_root] == -1:
                        continue 

                    union_root = find(roots, new_root)
                    if root != union_root:
                        roots[root] = union_root
                        root = union_root
                        count -= 1

            res.append(count)
        return res 


def find(roots, id):
    while roots[id] != id:
        roots[id] = roots[roots[id]]
        id = roots[id]
    return id



s = Solution()

m = 3
n = 3
positions = [[0,0], [0,1], [1,2], [2,1]]
res = s.numIslands2(m, n, positions)
exp = [1,1,2,3]
print(res, res == exp)


m = 3
n = 3
positions = [[0,0],[0,1],[1,2],[1,2]]
res = s.numIslands2(m, n, positions)
exp = [1,1,2,2]
print(res, res == exp)

m = 3
n = 3
positions = [[0,0],[0,1],[1,2],[0,1],[2,1]]
res = s.numIslands2(m, n, positions)
exp = [1,1,2,2,3]
print(res, res == exp)
