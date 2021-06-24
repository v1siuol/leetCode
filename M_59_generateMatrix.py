from __future__ import annotations 
import collections 
import random 
import heapq 
import math



# class Solution:
#   def generateMatrix(self, n):
#       """
#       :type n: int
#       :rtype: List[List[int]]
#       """

#       """
#       35min 
#       O(n^2)
#       模拟方向走 
#       Runtime: 68 ms, faster than 10.38% of Python3 online submissions for Spiral Matrix II.
#       discuss 有神仙写法 
#       """
#       curr_row = 0
#       curr_col = 0
#       curr_val = 1
#       ret_lst = [[1 for _ in range(n)] for _ in range(n)]
#       right_bound = n
#       bot_bound = n 
#       top_bound = 1
#       left_bound = 0

#       iter_count = 0

#       while iter_count < n-1: #i < n

#           # go right 
#           while curr_col < right_bound:
#               ret_lst[curr_row][curr_col] = curr_val
#               curr_col += 1 
#               curr_val += 1
#           curr_col -= 1 
#           right_bound -= 1

#           # go down 
#           curr_row += 1 
#           while curr_row < bot_bound:
#               ret_lst[curr_row][curr_col] = curr_val
#               curr_row += 1 
#               curr_val += 1
#           curr_row -= 1 
#           bot_bound -= 1

#           # go left 
#           curr_col -= 1
#           while curr_col >= left_bound:
#               ret_lst[curr_row][curr_col] = curr_val
#               curr_col -= 1
#               curr_val += 1
#           curr_col += 1
#           left_bound += 1

#           # go up
#           curr_row -= 1
#           while curr_row >= top_bound:
#               ret_lst[curr_row][curr_col] = curr_val
#               curr_row -= 1
#               curr_val += 1
#           curr_row += 1
#           top_bound += 1

#           curr_col += 1
#           iter_count += 1 

#       return ret_lst 

        
# sol = Solution()
# print(sol.generateMatrix(1))
# print(sol.generateMatrix(2))
# print(sol.generateMatrix(3))
# print(sol.generateMatrix(4))



"""
Success
Details 
Runtime: 32 ms, faster than 91.19% of Python3 online submissions for Spiral Matrix II.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Spiral Matrix II.
"""
# class Solution:
#     def generateMatrix(self, n: int) -> List[List[int]]:
#         # sim seem to have optimize 
#         directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # right bot left top
#         i = 0
#         j = 0
        
#         c1 = 0
#         r1 = 0
#         c2 = n-1
#         r2 = n-1
#         ret = [[0] * n for _ in range(n)]
#         for x in range(n*n):
#             ret[i][j] = x+1
#             d = 0

#             if i == r1 and c1 <= j < c2:
#                 d = 0
#             elif r1 <= i < r2 and j == c2:
#                 d = 1
#             elif i == r2 and c1 < j <= c2:
#                 d = 2
#             else:
#                 if r1 == i-1:
#                     d = 0
#                     r1 += 1
#                     c1 += 1
#                     r2 -= 1
#                     c2 -= 1
#                 else:
#                     d = 3
                    
#             i += directions[d][0]
#             j += directions[d][1]
            
#         return ret


"""
Success
Details 
Runtime: 28 ms, faster than 97.42% of Python3 online submissions for Spiral Matrix II.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Spiral Matrix II.
"""
# 看不懂的 diss
# class Solution:
#     def generateMatrix(self, n: int) -> List[List[int]]:
#         A, lo = [], n*n+1
#         while lo > 1:
#             lo, hi = lo - len(A), lo
#             A = [range(lo, hi)] + list(zip(*A[::-1]))
#         return A


"""
Success
Details 
Runtime: 20 ms, faster than 99.97% of Python3 online submissions for Spiral Matrix II.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Spiral Matrix II.
Next challeng
"""
# better walk 
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        i = 0
        j = 0
        di = 0
        dj = 1

        matrix = [ [0] * n for _ in range(n) ]
        for x in range(n * n):
            matrix[i][j] = x+1

            # turn
            if matrix[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di

            i += di
            j += dj

        return matrix
