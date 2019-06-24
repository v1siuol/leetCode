"""
Success
Details 
Runtime: 1168 ms, faster than 8.88% of Python3 online submissions for Shortest Distance from All Buildings.
Memory Usage: 13.2 MB, less than 66.76% of Python3 online submissions for Shortest Distance from All Buildings.
"""
from __future__ import annotations 
from copy import deepcopy

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        walk = 0 
        # total = [i[:] for i in grid[:]]
        total = deepcopy(grid)

        direction = [(0,-1), (1,0), (0,1), (-1,0)]
        min_dist = -1 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:  
                    # found building 
                    min_dist = -1
                    # dist = [i[:] for i in grid[:]]
                    dist = deepcopy(grid)

                    lst = []
                    lst.append([i, j])
                    while lst:
                        loc = lst.pop(0)
                        for d in direction:
                            next_i = loc[0] + d[0]
                            next_j = loc[1] + d[1]
                            if next_i >= 0 and next_i < m and next_j >= 0 and next_j < n and grid[next_i][next_j] == walk:
                                grid[next_i][next_j] -= 1 
                                dist[next_i][next_j] = dist[loc[0]][loc[1]] + 1
                                total[next_i][next_j] += dist[next_i][next_j] - 1 
                                lst.append([next_i, next_j])
                                # min_dist = min(min_dist, total[next_i][next_j])
                                if min_dist < 0 or min_dist > total[next_i][next_j]:
                                    min_dist = total[next_i][next_j]
                                # print(dist)
                    walk -= 1
        return min_dist




s = Solution()

print(s.shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]))
