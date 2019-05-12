"""
Success
Details 
Runtime: 32 ms, faster than 99.68% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
Memory Usage: 13.4 MB, less than 6.58% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
"""
class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        buy = float('-inf')
        rest = 0
        sell = 0
        for price in prices:
            prev_sell = sell
            sell = max(sell, buy+price)
            buy = max(buy, rest-price)
            rest = max(rest, prev_sell)
        return sell




s = Solution()
print(s.maxProfit([1,2,3,0,2]))
print(s.maxProfit([1]))


