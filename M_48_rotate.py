"""
Success
Details 
Runtime: 36 ms, faster than 89.58% of Python3 online submissions for Rotate Image.
Memory Usage: 12.9 MB, less than 97.76% of Python3 online submissions for Rotate Image.
"""
from __future__ import annotations 

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2 + n%2):
            for j in range(n//2):
                matrix[i][j], matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i] = matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i], matrix[i][j]




s = Solution()

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

s.rotate(matrix)
print(matrix)


matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
] 

s.rotate(matrix)
print(matrix)

