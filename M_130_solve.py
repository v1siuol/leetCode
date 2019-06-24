"""
Success
Details 
Runtime: 108 ms, faster than 99.46% of Python3 online submissions for Surrounded Regions.
Memory Usage: 15 MB, less than 33.10% of Python3 online submissions for Surrounded Regions.
"""
from __future__ import annotations 
import collections 


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check(i, j):
            if board[i][j] == 'O':
                board[i][j] = 'S'
                if i > 0:
                    check(i-1, j)
                if i < m-1:
                    check(i+1, j)
                if j > 0:
                    check(i, j-1)
                if j < n-1:
                    check(i, j+1)

        m = len(board)
        if m == 0:
            return 
        n = len(board[0])

        # left right col 
        for i in range(m):
            check(i, 0)
            if m > 1:
                check(i, n-1)

        # top bot row 
        for j in range(n):
            check(0, j)
            if n > 1:
                check(m-1, j)

        for i, row in enumerate(board):
            for j, loc in enumerate(row):
                if loc == 'O':
                    board[i][j] = 'X'

        for i, row in enumerate(board):
            for j, loc in enumerate(row):
                if loc == 'S':
                    board[i][j] = 'O'

        


    # # TLE 
    # def solve(self, board: List[List[str]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #     def dfs(ij, temp, flag):
    #         temp.append(ij)
    #         if ij[0] == 0 or ij[0] == len(board)-1 or ij[1] == 0 or ij[1] == len(board[0]) - 1:
    #             flag = True 
    #         for k in range(1, 5):
    #             next_ij = (ij[0] + delta[k-1], ij[1] + delta[k])
    #             if next_ij in o_queue:
    #                 o_queue.remove(next_ij)
    #                 flag = dfs(next_ij, temp, flag) or flag 

    #         return flag 

    #     delta = [0, 1, 0, -1, 0]
    #     o_set = set()
    #     o_queue = collections.deque()
    #     for i, row in enumerate(board):
    #         for j, loc in enumerate(row):
    #             if loc == 'O':
    #                 o_set.add((i,j))
    #                 o_queue.append((i,j))
    #     while o_queue:
    #         temp = collections.deque()
    #         ij = o_queue.pop()
    #         if not dfs(ij, temp, False):
    #             for i, j in temp:
    #                 board[i][j] = 'X'

s = Solution()

# lst = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# s.solve(lst)
# print(lst)

# lst = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
# s.solve(lst)
# print(lst)


lst = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
s.solve(lst)
print(lst)