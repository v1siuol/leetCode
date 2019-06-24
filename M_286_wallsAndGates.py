"""
Success
Details 
Runtime: 220 ms, faster than 67.59% of Python3 online submissions for Walls and Gates.
Memory Usage: 16.1 MB, less than 44.18% of Python3 online submissions for Walls and Gates.
"""
from __future__ import annotations 
from collections import deque  

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return 
        ROOM = 2147483647 
        GATE = 0
        q = deque()
        m = len(rooms)
        n = len(rooms[0])
        delta = [0, 1, 0, -1, 0]

        for i, row in enumerate(rooms):
            for j, loc in enumerate(row):
                if loc == GATE:
                    q.append([i,j])

        while q:
            i, j = q.popleft()
            for k in range(1, 5):
                next_i = i+delta[k-1]
                next_j = j+delta[k]
                if 0 <= next_i < m and 0 <= next_j < n and rooms[next_i][next_j] == ROOM:
                    rooms[next_i][next_j] = rooms[i][j] + 1
                    q.append([next_i, next_j])



s = Solution()

lst = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
s.wallsAndGates(lst)
print(lst)



lst = [
    [-1,0,2147483647],
    [2147483647,-1,2147483647],
    [2147483647,2147483647,2147483647]
]
s.wallsAndGates(lst)
print(lst)  # [[-1,0,1],[6,-1,2],[5,4,3]]


lst = []
s.wallsAndGates(lst)
print(lst)  
