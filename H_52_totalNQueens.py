from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 52 ms, faster than 85.34% of Python3 online submissions for N-Queens II.
Memory Usage: 13.2 MB, less than 34.28% of Python3 online submissions for N-Queens II.
"""

# class Solution:
#     def totalNQueens(self, n: int) -> int:
#         def dfs(col_set, xy_sum, xy_dif, count):
#             if count == n:
#                 return 1 
#             res = 0
#             for q in range(n):
#                 if q not in col_set and (count-q) not in xy_dif and (count+q) not in xy_sum:
#                     col_set.add(q)
#                     xy_dif.add(count-q)
#                     xy_sum.add(count+q)
#                     res += dfs(col_set, xy_sum, xy_dif, count+1)
#                     col_set.remove(q)
#                     xy_dif.remove(count-q)
#                     xy_sum.remove(count+q)
#             return res

#         xy_dif_set = set()
#         xy_sum_set = set()
#         col_set = set()
#         return dfs(col_set, xy_sum_set, xy_dif_set, 0)


# s = Solution()

# print(s.totalNQueens(4))
# print(s.totalNQueens(5))


"""
Success
Details 
Runtime: 48 ms, faster than 91.89% of Python3 online submissions for N-Queens II.
Memory Usage: 13.7 MB, less than 5.31% of Python3 online submissions for N-Queens II.
"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        return backtrack([], [], [], n)

def backtrack(queens, xy_sum, xy_dif, n):
    p = len(queens)
    if p == n:
        return 1 
    count = 0
    for q in range(n):
        if q not in queens and (p+q) not in xy_sum and (p-q) not in xy_dif:
            count += backtrack(queens+[q], xy_sum+[p+q], xy_dif+[p-q], n)
    return count 
