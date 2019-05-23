"""
Success
Details 
Runtime: 1308 ms, faster than 59.57% of Python3 online submissions for Coin Change.
Memory Usage: 13.3 MB, less than 46.41% of Python3 online submissions for Coin Change.
"""
class Solution:
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        # dfs.. 快？ 
        dp = [amount+1] * (amount+1)  # to rebute after
        dp[0] = 0

        i = 1
        while i <= amount:
            for coin in coins:
                if i >= coin: 
                    dp[i] = min(dp[i], dp[i-coin] + 1)

            i += 1
            # print(dp)

        return -1 if dp[amount] > amount else dp[amount] 



S = Solution()
print(S.coinChange([1, 2, 5], 11))
print(S.coinChange([2], 3))
print(S.coinChange([1], 0))
print(S.coinChange([2,5,10,1], 27))


