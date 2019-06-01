"""
Success
Details 
Runtime: 72 ms, faster than 97.95% of Python3 online submissions for Maximal Square.
Memory Usage: 14 MB, less than 34.97% of Python3 online submissions for Maximal Square.
"""
from __future__ import annotations

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        M = len(matrix)
        N = len(matrix[0]) if M > 0 else 0
        dp = [0] * (N+1)
        max_sqr = 0
        for i in range(1, M+1):
            prev = 0
            for j in range(1, N+1):
                temp = dp[j]
                if matrix[i-1][j-1] == '1':
                    dp[j] = min(dp[j-1], dp[j], prev) + 1
                    max_sqr = max(max_sqr, dp[j])
                else:
                    dp[j] = 0

                prev = temp

        return max_sqr * max_sqr


s = Solution()
print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
# print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
