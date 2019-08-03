from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        i = 0
        j = 0
        board = dict()
        for c in 'abcdefghijklmnopqrstuvwxyz':
            board[c] = (j, i)
            i += 1
            if i == 5:
                i = 0
                j += 1

        res = ''
        loc = (0, 0)
        i = 0
        while i < len(target) and target[i] == 'a':
            res += '!'
            i += 1
        while i < len(target):
            new_x, new_y = board[target[i]]

            if i > 0 and target[i-1] == 'z':
                # z case 
                if new_x > loc[0]:
                    res += 'D' * (new_x - loc[0])
                elif new_x < loc[0]:
                    res += 'U' * abs(new_x - loc[0])
                if new_y > loc[1]:
                    res += 'R' * (new_y - loc[1])
                elif new_y < loc[1]:
                    res += 'L' * abs(new_y - loc[1])
            else:
                # normal 
                if new_y > loc[1]:
                    res += 'R' * (new_y - loc[1])
                elif new_y < loc[1]:
                    res += 'L' * abs(new_y - loc[1])

                if new_x > loc[0]:
                    res += 'D' * (new_x - loc[0])
                elif new_x < loc[0]:
                    res += 'U' * abs(new_x - loc[0])

            res += '!'
            loc = (new_x, new_y)
            i += 1

        return res


s = Solution()

target = "leet"
print(s.alphabetBoardPath(target))

target = "code"
print(s.alphabetBoardPath(target))

target = "a"
print(s.alphabetBoardPath(target))


target = ""
print(s.alphabetBoardPath(target))

target = "zb"
print(s.alphabetBoardPath(target))

target = "zdz"
print(s.alphabetBoardPath(target))
