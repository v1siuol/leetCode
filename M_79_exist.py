"""
Success
Details 
Runtime: 336 ms, faster than 22.16% of Python3 online submissions for Word Search.
Memory Usage: 14.3 MB, less than 54.68% of Python3 online submissions for Word Search.
"""
from __future__ import annotations 

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # backtracking 
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(board, i, j, word):
                    return True 
        return False 


def helper(board, i, j, word):
    if len(word) == 0:
        return True 
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
        return False 
    temp = board[i][j]
    board[i][j] = None 
    res = helper(board, i+1, j, word[1:]) or helper(board, i-1, j, word[1:]) or helper(board, i, j+1, word[1:]) or helper(board, i, j-1, word[1:])
    board[i][j] = temp
    return res 




s = Solution()

board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]

print(s.exist(board, 'ABCCED'))  # True 
print(s.exist(board, 'SEE'))  # True 
print(s.exist(board, 'ABCB'))  # False  

