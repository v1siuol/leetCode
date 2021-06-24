from __future__ import annotations 
import collections 
import random 
import heapq 
import re
import threading


"""
Success
Details 
Runtime: 336 ms, faster than 12.98% of Python3 online submissions for Knight Probability in Chessboard.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Knight Probability in Chessboard.
"""
# 反向 
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        # dp? O(kn^2)
        dp = [ [1] * N for _ in range(N) ]
        moves = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
        for _ in range(K):
            next_dp = [ [0] * (N) for _ in range(N) ]
            for i in range(N):
                for j in range(N):
                    for di, dj in moves:
                        if is_legal(N, i+di, j+dj):
                            next_dp[i][j] += dp[i+di][j+dj]
            dp = next_dp

        return dp[r][c] / (8 ** K)


def is_legal(N, r, c):
    return 0 <= r < N and 0 <= c < N
