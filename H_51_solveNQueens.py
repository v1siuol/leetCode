from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 60 ms, faster than 95.46% of Python3 online submissions for N-Queens.
Memory Usage: 13.4 MB, less than 69.54% of Python3 online submissions for N-Queens.
"""

# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         def dfs(queens, xy_sum, xy_dif):
#             p = len(queens)
#             if p == n:
#                 res.append(queens)
#                 return 
#             for q in range(n):
#                 if q not in queens and (p-q) not in xy_dif and (p+q) not in xy_sum:
#                     dfs(queens+[q], xy_sum+[p+q], xy_dif+[p-q])

#         res = []
#         dfs([], [], [])
#         return [['.'*i+'Q'+'.'*(n-i-1) for i in sol] for sol in res]


# s = Solution()
# print(s.solveNQueens(4))


"""
Success
Details 
Runtime: 60 ms, faster than 94.66% of Python3 online submissions for N-Queens.
Memory Usage: 14.1 MB, less than 5.50% of Python3 online submissions for N-Queens.

"""

# index 是 row queens 里是 col 
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []
        dfs([], [], [], n, ret)
        return [['.'*i+'Q'+'.'*(n-i-1) for i in sol] for sol in ret]


def dfs(queens, xy_sum, xy_dif, n, ret):
    p = len(queens)
    if p == n:
        ret.append(queens)
        return 
    for q in range(n):
        if q not in queens and (p-q) not in xy_dif and (p+q) not in xy_sum:
            dfs(queens+[q], xy_sum+[p+q], xy_dif+[p-q], n, ret)
