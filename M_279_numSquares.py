"""
Success
Details 
Runtime: 88 ms, faster than 95.12% of Python3 online submissions for Perfect Squares.
Memory Usage: 13.3 MB, less than 62.86% of Python3 online submissions for Perfect Squares.
"""
class Solution:
    _dp = [0]
    def numSquares(self, n: 'int') -> 'int':
        # .. 后往前看 
        dp = self._dp
        while len(dp) <= n:
            # print(dp)
            dp.append(min(dp[-i*i] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1)
        return dp[n]




s = Solution()

print(s.numSquares(7))
print(s.numSquares(12))
print(s.numSquares(13))
print(s.numSquares(35))
