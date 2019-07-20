from __future__ import annotations 
import collections 
import random 
import heapq 


"""
Runtime: 280 ms
Memory Usage: 14.9 MB
You are here! 
Your runtime beats 52.35 % of python3 submissions.
"""
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # BIT  // time should be O(log(m) * log(n))
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.tree = [[0] * (self.n+1) for _ in range(self.m+1)]
        self.nums = [[0] * self.n for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        if self.m == 0 or self.n == 0:
            return 
        delta = val - self.nums[row][col]
        self.nums[row][col] = val 

        i = row + 1 
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.tree[i][j] += delta
                j += j&(-j)
            i += i&(-i)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.m == 0 or self.n == 0:
            return 
        return self._sum(row2+1, col2+1) + self._sum(row1, col1) - self._sum(row1, col2+1) - self._sum(row2+1, col1)

    def _sum(self, row, col):
        s = 0

        i = row 
        while i > 0:
            j = col 
            while j > 0:
                s += self.tree[i][j]
                j -= j&(-j)
            i -= i&(-i)
        return s


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)