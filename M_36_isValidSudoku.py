from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 48 ms, faster than 84.88% of Python3 online submissions for Valid Sudoku.
Memory Usage: 13.3 MB, less than 11.16% of Python3 online submissions for Valid Sudoku.
"""

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         row = [set() for _ in range(9)]
#         col = [set() for _ in range(9)]
#         box = [set() for _ in range(9)]
#         for i in range(9):
#             for j in range(9):
#                 num = board[i][j]
#                 if num != '.':
#                     if num in row[i]:
#                         return False 
#                     row[i].add(num)
#                     if num in col[j]:
#                         return False
#                     col[j].add(num)

#                     k = i // 3 * 3 + j // 3 

#                     if num in box[k]:
#                         return False
#                     box[k].add(num)

#         return True  


# s = Solution()

# lst = [
#     ["8","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]
# ]

# print(s.isValidSudoku(lst))  # false 

# lst = [
#     ["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]
# ]

# print(s.isValidSudoku(lst))  # true 


"""
Success
Details 
Runtime: 40 ms, faster than 98.06% of Python3 online submissions for Valid Sudoku.
Memory Usage: 13.7 MB, less than 5.58% of Python3 online submissions for Valid Sudoku.
"""

"""
'4' in row 7 is encoded as "(4)7".
'4' in column 7 is encoded as "7(4)".
'4' in the top-right block is encoded as "0(4)2"
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num != '.':
                    b = '(' + str(num) + ')'

                    r = b + str(i)
                    c = str(j) + b
                    b = str(i//3) + b + str(j//3)

                    if r in seen or c in seen or b in seen:
                        return False

                    seen.add(r)
                    seen.add(c)
                    seen.add(b)

        return True 
