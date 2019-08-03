from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 848 ms, faster than 43.12% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
Memory Usage: 20.6 MB, less than 10.23% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
"""

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash
