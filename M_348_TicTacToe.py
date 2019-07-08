"""
Success
Details 
Runtime: 52 ms, faster than 98.45% of Python3 online submissions for Design Tic-Tac-Toe.
Memory Usage: 15.4 MB, less than 75.72% of Python3 online submissions for Design Tic-Tac-Toe.
"""

from __future__ import annotations 
import collections 
import random 
import heapq 

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.row = [0] * n
        self.col = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        n = self.n

        move = 1 if player == 1 else -1 
        self.row[row] += move 
        if self.row[row] == n or self.row[row] == -n:
            return player
        self.col[col] += move 
        if self.col[col] == n or self.col[col] == -n:
            return player

        if row == col:
            self.diagonal += move
            if self.diagonal == n or self.diagonal == -n:
                return player

        if row + col == n-1:
            self.anti_diagonal += move
            if self.anti_diagonal == n or self.anti_diagonal == -n:
                return player

        return 0 


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)