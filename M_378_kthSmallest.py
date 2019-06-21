"""
Success
Details 
Runtime: 48 ms, faster than 95.10% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 17.4 MB, less than 44.66% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
"""
from __future__ import annotations 

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 迷糊 
        lo = matrix[0][0]
        hi = matrix[-1][-1] + 1
        n = len(matrix[0])
        while lo < hi:
            mid = (lo + hi) // 2
            count = 0
            j = n - 1
            for i in range(len(matrix)):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += (j+1)
            if count < k:
                lo = mid + 1
            else:
                hi = mid 
        return lo 


s = Solution()

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8

print(s.kthSmallest(matrix, k))
