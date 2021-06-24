from __future__ import annotations 
import collections 
import random 
import heapq 


"""
Success
Details 
Runtime: 100 ms, faster than 68.62% of Python3 online submissions for Maximal Rectangle.
Memory Usage: 14 MB, less than 27.87% of Python3 online submissions for Maximal Rectangle.
"""

# class Solution:
#     def maximalRectangle(self, matrix: List[List[str]]) -> int:
#         M = len(matrix)
#         if M > 0:
#             N = len(matrix[0])
#         else:
#             N = 0
#         max_area = 0
#         height = [0]*N
#         left = [0]*N
#         right = [N]*N
#         for row in range(M):

#             curr_left = 0
#             curr_right = N

#             for col in range(N):
#                 if matrix[row][col] == '1': 
#                     height[col] += 1
#                     left[col] = max(left[col], curr_left)
#                 else:
#                     height[col] = 0
#                     left[col] = 0
#                     curr_left = col + 1

#                 if matrix[row][~col] == '1':
#                     right[~col] = min(right[~col], curr_right)
#                 else:
#                     curr_right = N-col-1
#                     right[~col] = N

#             for col in range(N):
#                 max_area = max(max_area, height[col] * (right[col]-left[col]))
 

#             # print(height)
#             # print(left)
#             # print(right)
#             # print()

#         return max_area




# s = Solution()

# inp = [
#   ["0","0","0","1","0","0","0"],
#   ["0","0","1","1","1","0","0"],
#   ["0","1","1","1","1","1","0"]
# ]
# print(s.maximalRectangle(inp))  # 3

# inp = [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# print(s.maximalRectangle(inp))  # 6


# inp = [
#   ["1","1","1","0","0"],
#   ["1","1","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# print(s.maximalRectangle(inp))  # 10
