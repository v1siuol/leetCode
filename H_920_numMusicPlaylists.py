from __future__ import annotations 
import collections 
import random 
import heapq 


"""
Success
Details 
Runtime: 84 ms, faster than 65.68% of Python3 online submissions for Number of Music Playlists.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Number of Music Playlists.
"""
# dp
class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        dp = [[0]*(N+1) for _ in range(L+1)]
        dp[0][0] = 1
        m = 10 ** 9 + 7

        for i in range(1, L+1):
            for j in range(1, N+1):
                dp[i][j] = (dp[i-1][j-1] * (N-j+1) % m)  # new 
                if j > K:
                    dp[i][j] += (dp[i-1][j] * (j-K) % m)  # old 
                    dp[i][j] %= m

        return dp[L][N]
