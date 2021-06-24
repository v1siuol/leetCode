from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 36 ms, faster than 81.24% of Python3 online submissions for Game of Life.
Memory Usage: 13.8 MB, less than 5.25% of Python3 online submissions for Game of Life.
"""

"""
神仙 diss 
1的cell 旁边少于2个 die 
1的cell 2/3 活着
1的cell 多于3个 die 
0的cell 3个live 1 
"""

# class Solution:
#     def gameOfLife(self, board: List[List[int]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         m = len(board)
#         n = len(board[0])

#         for i in range(m):
#             for j in range(n):
#                 lives = get_live_neighbors(board, m, n, i, j)

#                 if board[i][j] == 1 and 2 <= lives <= 3:
#                     board[i][j] = 3  # 11 
#                 if board[i][j] == 0 and lives == 3:
#                     board[i][j] = 2  # 10 

#         for i in range(m):
#             for j in range(n):
#                 board[i][j] >>= 1 


# def get_live_neighbors(board, m, n, i, j):
#     lives = 0
#     for x in range(max(0, i-1), min(m-1, i+1)+1):
#         for y in range(max(0, j-1), min(n-1, j+1)+1):
#             lives += board[x][y] & 1  # 01 
#     lives -= board[i][j] & 1
#     return lives 


"""
Success
Details 
Runtime: 32 ms, faster than 97.86% of Python3 online submissions for Game of Life.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Game of Life.
"""
"""
二进制嚯
"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        for x in range(m):
            for y in range(n):
                lives = get_live(board, x, y, m, n)
                if board[x][y] == 1 and 2 <= lives <= 3:
                    board[x][y] = 3  # 11
                elif board[x][y] == 0 and lives == 3:
                    board[x][y] = 2

        for x in range(m):
            for y in range(n):
                board[x][y] >>= 1

        return board


def get_live(board, i, j, m, n):
    lives = 0
    for x in range(max(0, i-1), min(m, i+2)):
        for y in range(max(0, j-1), min(n, j+2)):
            lives += board[x][y] & 1  # current 
    lives -= board[i][j] & 1
    return lives
