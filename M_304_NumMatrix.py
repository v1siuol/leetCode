"""
Success
Details 
Runtime: 60 ms, faster than 68.68% of Python3 online submissions for Range Sum Query 2D - Immutable.
Memory Usage: 15.8 MB, less than 64.01% of Python3 online submissions for Range Sum Query 2D - Immutable.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return 
        self.dp = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dp[i+1][j+1] = self.dp[i][j+1] + self.dp[i+1][j] - self.dp[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)