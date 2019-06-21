"""
Success
Details 
Runtime: 212 ms, faster than 98.47% of Python3 online submissions for Longest Increasing Path in a Matrix.
Memory Usage: 14 MB, less than 54.81% of Python3 online submissions for Longest Increasing Path in a Matrix.
"""
from __future__ import annotations 

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i+1, j) if i < m-1 and val > matrix[i+1][j] else 0,
                    dfs(i-1, j) if i > 0 and val > matrix[i-1][j] else 0,
                    dfs(i, j+1) if j < n-1 and val > matrix[i][j+1] else 0,
                    dfs(i, j-1) if j > 0 and val > matrix[i][j-1] else 0)
            return dp[i][j]


        if not matrix or not matrix[0]:
            return 0 

        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * n for _ in range(m)]

        return max(dfs(x, y) for x in range(m) for y in range(n))




s = Solution()

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
print(s.longestIncreasingPath(nums))

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
print(s.longestIncreasingPath(nums))
