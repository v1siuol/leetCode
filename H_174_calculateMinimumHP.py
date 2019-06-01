"""
Success
Details 
Runtime: 56 ms, faster than 47.20% of Python3 online submissions for Dungeon Game.
Memory Usage: 13.8 MB, less than 63.00% of Python3 online submissions for Dungeon Game.
"""
from __future__ import annotations

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp = [[0] * len(dungeon[0]) for _ in range(len(dungeon))]

        for i in range(len(dungeon)-1, -1, -1):
            for j in range(len(dungeon[0])-1, -1, -1):
                if i == len(dungeon)-1 and j == len(dungeon[0])-1:
                    if dungeon[i][j] <= 0:
                        dp[i][j] = abs(dungeon[i][j]) + 1
                    else:
                        dp[i][j] = 1
                elif i == len(dungeon)-1:
                    temp = dp[i][j+1] - dungeon[i][j]
                    dp[i][j] = 1 if temp <= 0 else temp
                elif j == len(dungeon[0])-1:
                    temp = dp[i+1][j] - dungeon[i][j]
                    dp[i][j] = 1 if temp <= 0 else temp
                else:
                    temp = min(dp[i][j+1] - dungeon[i][j], dp[i+1][j] - dungeon[i][j])
                    dp[i][j] = 1 if temp <= 0 else temp

        return dp[0][0]



s = Solution()
print(s.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
print(s.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5],[10,30,-5]]))
