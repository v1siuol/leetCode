"""
Success
Details 
Runtime: 180 ms, faster than 13.61% of Python3 online submissions for Sparse Matrix Multiplication.
Memory Usage: 13.3 MB, less than 80.26% of Python3 online submissions for Sparse Matrix Multiplication.
"""
from __future__ import annotations 

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # partial ? 
        m1 = len(A)
        n1 = len(A[0])
        m2 = len(B)
        n2 = len(B[0])

        res = [[0] * n2 for _ in range(m1)]
        for m in range(m1):
            for n in range(n2):
                res[m][n] = sum(A[m][k] * B[k][n] for k in range(n1))

        return res 


s = Solution()

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

print(s.multiply(A, B))
