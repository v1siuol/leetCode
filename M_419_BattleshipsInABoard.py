"""
28 / 28 test cases passed.
Status: Accepted
Runtime: 36 ms
You are here! 
Your runtime beats 43.15 % of python submissions.
"""
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if len(board)<=0:
            return 0
        m = len(board)
        n = len(board[0])
        x, y = 0, 0
        count = 0

        lst_checked = [[False for _ in range(n)] for _ in range(m)]
        while x < m:
            y = 0
            while y < n:
                if not lst_checked[x][y]:
                    if board[x][y] == 'X':
                        temp = x
                        while temp+1 < m:
                            if not lst_checked[temp+1][y]:
                                if board[temp+1][y] == 'X':
                                    lst_checked[temp+1][y] = True
                                    temp += 1
                                else:
                                    lst_checked[temp+1][y] = True
                                    break
                            else:
                                break

                        temp = y
                        while temp+1 < n:
                            if not lst_checked[x][temp+1]:
                                if board[x][temp+1] == 'X':
                                    lst_checked[x][temp+1] = True
                                    temp += 1
                                else:
                                    lst_checked[x][temp+1] = True
                                    break
                            else:
                                break
                            
                        count += 1

                lst_checked[x][y] = True
                y += 1
            x += 1

        return count

# print(Solution().countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))
t1 = [[".","X"],["X","."]]
print(Solution().countBattleships(t1))
