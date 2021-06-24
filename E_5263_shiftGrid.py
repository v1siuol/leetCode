from __future__ import annotations 
import collections 
import random 
import heapq 


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # sim 
        m = len(grid)
        n = len(grid[0])
        for _ in range(k):
            last_column = []
            for i in range(m):
                last_column.append(grid[i][-1])

            for j in reversed(range(1, n)):
                for i in range(m):
                    grid[i][j] = grid[i][j-1]

            # print(last_column, grid)
            for i in range(1, m):
                grid[i][0] = last_column[i-1]

            grid[0][0] = last_column[-1]

        return grid


s = Solution()

grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(s.shiftGrid(grid, k) == [[9, 1, 2], [3, 4, 5], [6, 7, 8]])

grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 9
print(s.shiftGrid(grid, k) == [[1,2,3],[4,5,6],[7,8,9]])

grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4
print(s.shiftGrid(grid, k) == [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]])

grid = [[1],[2],[3],[4],[7],[6],[5]]
k = 23
print(s.shiftGrid(grid, k) == [[6],[5],[1],[2],[3],[4],[7]])

# [[6],[5],[1],[2],[3],[4],[7]]
