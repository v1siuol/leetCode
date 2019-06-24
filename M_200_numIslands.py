"""
Success
Details 
Runtime: 76 ms, faster than 80.70% of Python3 online submissions for Number of Islands.
Memory Usage: 14.1 MB, less than 43.50% of Python3 online submissions for Number of Islands.
"""
from __future__ import annotations 


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs 
        def dfs(i, j):
            if i >= 0 and i < m and j >= 0 and j < n and grid[i][j] == '1':
                grid[i][j] = '0'
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)
                return True 
            return False 

        if not grid or not grid[0]:
            return 0 
        res = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if dfs(i, j):
                    res += 1
        return res 



s = Solution()


lst = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(s.numIslands(lst))  

lst = [["1"],["1"]]
print(s.numIslands(lst))  