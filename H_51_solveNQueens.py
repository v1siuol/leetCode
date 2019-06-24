"""
Success
Details 
Runtime: 60 ms, faster than 95.46% of Python3 online submissions for N-Queens.
Memory Usage: 13.4 MB, less than 69.54% of Python3 online submissions for N-Queens.
"""
from __future__ import annotations 
import collections 

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queens, xy_sum, xy_dif):
            p = len(queens)
            if p == n:
                res.append(queens)
                return 
            for q in range(n):
                if q not in queens and (p-q) not in xy_dif and (p+q) not in xy_sum:
                    dfs(queens+[q], xy_sum+[p+q], xy_dif+[p-q])

        res = []
        dfs([], [], [])
        return [['.'*i+'Q'+'.'*(n-i-1) for i in sol] for sol in res]





s = Solution()

print(s.solveNQueens(4))
