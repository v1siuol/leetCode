"""
Success
Details 
Runtime: 132 ms, faster than 74.93% of Python3 online submissions for Bomb Enemy.
Memory Usage: 14 MB, less than 97.75% of Python3 online submissions for Bomb Enemy.
"""
from __future__ import annotations 

class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0 
        m = len(grid)
        n = len(grid[0])
        res = 0
        row_e = 0
        col_e = [0] * n 
        for i in range(m):
            for j in range(n):
                
                if j == 0 or grid[i][j-1] == 'W':
                    row_e = 0 
                    for k in range(j, n):
                        if grid[i][k] == 'W':
                            break 
                        if grid[i][k] == 'E':
                            row_e += 1 

                if i == 0 or grid[i-1][j] == 'W':
                    col_e[j] = 0
                    for k in range(i, m):
                        if grid[k][j] == 'W':
                            break 
                        if grid[k][j] == 'E':
                            col_e[j] += 1

                if grid[i][j] == '0':
                    res = max(res, row_e+col_e[j])

        return res


s = Solution()

# i = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
# print(s.maxKilledEnemies(i))  # 3 

i = [["E"],["E"],["E"]]
print(s.maxKilledEnemies(i))  # 3 
