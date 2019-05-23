"""
Success
Details 
Runtime: 748 ms, faster than 59.90% of Python3 online submissions for Guess Number Higher or Lower II.
Memory Usage: 14 MB, less than 50.94% of Python3 online submissions for Guess Number Higher or Lower II.
"""
class Solution:
    def getMoneyAmount(self, n: 'int') -> 'int':
        # 神仙 
        dp = [[0] * (n+1) for _ in range(n+1)]

        length = 2
        while length <= n:

            for i in range(1, n-length+2):
                temp = float('inf')
                for pivot in range(i, i+length-1):
                    res = pivot + max(dp[i][pivot-1], dp[pivot+1][i+length-1])
                    temp = min(temp, res)

                dp[i][i+length-1] = temp
            length += 1

        return dp[1][n]


s = Solution()
print(s.getMoneyAmount(10))
print(s.getMoneyAmount(3))

