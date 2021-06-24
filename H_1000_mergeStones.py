from __future__ import annotations 
import collections 
import random 
import heapq 
import re


"""
Success
Details 
Runtime: 52 ms, faster than 88.24% of Python3 online submissions for Minimum Cost to Merge Stones.
Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Minimum Cost to Merge Stones.
"""
# class Solution:
#     def mergeStones(self, stones: List[int], K: int) -> int:
#         n = len(stones)
#         inf = float('inf')
#         prefix = [0] * (n + 1)
#         for i in range(n):
#             prefix[i + 1] = prefix[i] + stones[i]

#         import functools

#         @functools.lru_cache(None)
#         def dp(i, j, m):
#             if (j - i + 1 - m) % (K - 1):
#                 return inf
#             if i == j:
#                 return 0 if m == 1 else inf
#             if m == 1:
#                 return dp(i, j, K) + prefix[j + 1] - prefix[i]
#             return min(dp(i, mid, 1) + dp(mid + 1, j, m - 1) for mid in range(i, j, K - 1))
#         res = dp(0, n - 1, 1)
#         return res if res < inf else -1


"""
Success
Details 
Runtime: 44 ms, faster than 98.16% of Python3 online submissions for Minimum Cost to Merge Stones.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Minimum Cost to Merge Stones.
"""
class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        if (n - 1) % (K - 1): 
            return -1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        dp = [[0] * n for _ in range(n)]

        for l in range(K, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                dp[i][j] = float('inf')

                for k in range(i, j, K-1):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])

                if (j - i) % (K - 1) == 0:
                    dp[i][j] += prefix[j + 1] - prefix[i]

        return dp[0][n-1]
