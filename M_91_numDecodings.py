from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 56 ms, faster than 9.88% of Python3 online submissions for Decode Ways.
Memory Usage: 13.8 MB, less than 18.60% of Python3 online submissions for Decode Ways.
"""

# class Solution:
#     def numDecodings(self, s: str) -> int:
#         if s == '':
#             return 0
#         n = len(s)
#         dp = [0] * (len(s)+1)
#         dp[0] = 1
#         dp[1] = 1 if s[0] != '0' else 0
#         for i in range(2, n+1):
#             first = int(s[i-1:i])
#             second = int(s[i-2:i])
#             if 1 <= first <= 9:
#                 dp[i] += dp[i-1]
#             if 10 <= second <= 26:
#                 dp[i] += dp[i-2]
#         return dp[n]

"""
Success
Details 
Runtime: 28 ms, faster than 98.86% of Python3 online submissions for Decode Ways.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Decode Ways.
"""
# dp 状态啊 
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        p = pp = 1
        for i in reversed(range(n)):
            curr = p if s[i] != '0' else 0
            if i < n-1 and (s[i] == '1' or s[i] == '2' and '0' <= s[i+1] <= '6'):
                curr += pp
            pp = p
            p = curr
        return 0 if len(s) == 0 else p
