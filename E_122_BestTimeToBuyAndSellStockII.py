"""
198 / 198 test cases passed.
Status: Accepted
Runtime: 45 ms
You are here!
Your runtime beats 83.68% of python submissions.
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        re = 0
        i = 1
        while i < len(prices):
            if prices[i] - prices[i-1] > 0:
                re += prices[i] - prices[i-1]
            i += 1
        return re

print(Solution().maxProfit([1, 7, 2, 3, 6, 7, 6, 7]))
