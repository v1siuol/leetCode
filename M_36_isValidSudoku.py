"""
Success
Details 
Runtime: 48 ms, faster than 84.88% of Python3 online submissions for Valid Sudoku.
Memory Usage: 13.3 MB, less than 11.16% of Python3 online submissions for Valid Sudoku.

"""
from __future__ import annotations 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    if num in row[i]:
                        return False 
                    row[i].add(num)
                    if num in col[j]:
                        return False
                    col[j].add(num)

                    k = i // 3 * 3 + j // 3 

                    if num in box[k]:
                        return False
                    box[k].add(num)

        return True  


s = Solution()

lst = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(s.isValidSudoku(lst))  # false 

lst = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(s.isValidSudoku(lst))  # true 
