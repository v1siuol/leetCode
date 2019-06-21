"""
Success
Details 
Runtime: 40 ms, faster than 92.96% of Python3 online submissions for Best Meeting Point.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Best Meeting Point.
"""
from __future__ import annotations 

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # kai mofa median 
        total = 0
        for grid in grid, zip(*grid):
            X = []
            for x, row in enumerate(grid):
                X += [x] * sum(row)
            total += sum(abs(x - X[len(X)//2]) for x in X)
        return total 


s = Solution()

i = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print(s.minTotalDistance(i))  # 6  

