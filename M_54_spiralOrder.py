from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 36 ms, faster than 79.31% of Python3 online submissions for Spiral Matrix.
Memory Usage: 13.4 MB, less than 5.09% of Python3 online submissions for Spiral Matrix.
"""

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         def helper(r1, c1, r2, c2):
#             for c in range(c1, c2+1):
#                 yield r1, c
#             for r in range(r1+1, r2+1):
#                 yield r, c2
#             if r1 < r2 and c1 < c2:
#                 for c in range(c2-1, c1, -1):
#                     yield r2, c
#                 for r in range(r2, r1, -1):
#                     yield r, c1 

#         if not matrix:
#             return []

#         res = []
#         r1, c1 = 0, 0
#         r2 = len(matrix)-1
#         c2 = len(matrix[0])-1


#         while r1 <= r2 and c1 <= c2:
#             for r, c in helper(r1, c1, r2, c2):
#                 res.append(matrix[r][c])

#             r1 += 1
#             r2 -= 1
#             c1 += 1
#             c2 -= 1

#         return res



# s = Solution()

# lst = [
#     [ 1, 2, 3 ],
#     [ 4, 5, 6 ],
#     [ 7, 8, 9 ]
# ]

# print(s.spiralOrder(lst))

# lst = [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]

# print(s.spiralOrder(lst))

# lst = [
#   [1, 2, 3, 4]
# ]

# print(s.spiralOrder(lst))

# lst = [
#   [1], 
#   [2], 
#   [3], 
#   [4]
# ]

# print(s.spiralOrder(lst))


"""
Success
Details 
Runtime: 32 ms, faster than 86.14% of Python3 online submissions for Spiral Matrix.
Memory Usage: 13.8 MB, less than 5.18% of Python3 online submissions for Spiral Matrix.
"""

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         if len(matrix) == 0 or len(matrix[0]) == 0:
#             return []
#         r1 = 0
#         c1 = 0
#         r2 = len(matrix) - 1
#         c2 = len(matrix[0]) - 1
#         ret = []

#         while r1 <= r2 and c1 <= c2:
#             for j in range(c1, c2+1):
#                 ret.append(matrix[r1][j])
#             for i in range(r1+1, r2+1):
#                 ret.append(matrix[i][c2])
#             if r1 < r2 and c1 < c2:
#                 for j in range(c2-1, c1,-1):
#                     ret.append(matrix[r2][j])
#                 for i in range(r2, r1,-1):
#                     ret.append(matrix[i][c1])

#             r1 += 1
#             r2 -= 1
#             c1 += 1
#             c2 -= 1

#         return ret 


"""
Success
Details 
Runtime: 28 ms, faster than 98.10% of Python3 online submissions for Spiral Matrix.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Spiral Matrix.
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []

        c1 = 0
        r1 = 0

        r2 = len(matrix)-1
        c2 = len(matrix[0]) -1

        res = []
        while c1 <= c2 and r1 <= r2:

            for j in range(c1, c2+1):
                res.append(matrix[r1][j])

            for i in range(r1+1, r2+1):
                res.append(matrix[i][c2])

            if r1 < r2 and c1 < c2:  # !!!! 

                for j in reversed(range(c1+1, c2)):
                    res.append(matrix[r2][j])

                for i in reversed(range(r1+1, r2+1)):
                    res.append(matrix[i][c1])

            c1 += 1
            r1 += 1
            c2 -= 1
            r2 -= 1

        return res
