from __future__ import annotations 
import collections 
import random 
import heapq 


"""
Success
Details 
Runtime: 48 ms, faster than 75.42% of Python3 online submissions for Search a 2D Matrix II.
Memory Usage: 17.5 MB, less than 90.20% of Python3 online submissions for Search a 2D Matrix II.
"""

# class Solution:
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         if len(matrix) == 0 or len(matrix[0]) == 0:
#             return False 

#         row = len(matrix) - 1
#         col = 0

#         while row >= 0 and col < len(matrix[0]):
#             val = matrix[row][col]
#             if val == target:
#                 return True
#             elif val < target:
#                 col += 1
#             else:
#                 row -= 1
#         return False 



# s = Solution()

# matrix = [
#     [1,   4,  7, 11, 15],
#     [2,   5,  8, 12, 19],
#     [3,   6,  9, 16, 22],
#     [10, 13, 14, 17, 24],
#     [18, 21, 23, 26, 30]
# ]

# print(s.searchMatrix(matrix, 5))  # true 
# print(s.searchMatrix(matrix, 20))  # false 


"""
Success
Details 
Runtime: 40 ms, faster than 31.43% of Python3 online submissions for Search a 2D Matrix II.
Memory Usage: 17.4 MB, less than 92.59% of Python3 online submissions for Search a 2D Matrix II.
"""
# pruning O(n) O(1)
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])

        row = m - 1
        col = 0

        while row >= 0 and col < n:
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                col += 1
            else:
                row -= 1

        return False
