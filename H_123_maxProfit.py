"""
Success
Details 
Runtime: 56 ms, faster than 84.33% of Python3 online submissions for Best Time to Buy and Sell Stock III.
Memory Usage: 14.1 MB, less than 15.57% of Python3 online submissions for Best Time to Buy and Sell Stock III.
"""
class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        # 太难 我觉得你还是不会
        h1 = float("-inf")
        h2 = float('-inf')
        r1 = 0
        r2 = 0
        for price in prices:
            r2 = max(r2, h2+price)
            h2 = max(h2, r1-price)
            r1 = max(r1, h1+price)
            h1 = max(h1, -price)
        return r2 


s = Solution()
print(s.maxProfit([3,3,5,0,0,3,1,4]))
print(s.maxProfit([1,2,3,4,5]))
print(s.maxProfit([7,6,4,3,1]))

