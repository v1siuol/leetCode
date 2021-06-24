from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
200 / 200 test cases passed.
Status: Accepted
Runtime: 49 ms
You are here!
Your runtime beats 77.91% of python submissions.
"""
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         """
#         re = 0
#         i = 0
#         while i < len(prices):
#             j = i + 1
#             while j < len(prices):
#                 n = prices[j] - prices[i]
#                 if re < n:
#                     re = n
#                 j += 1
#             i += 1
#         return re
#         """

# # 一步一步走 边搜 双指针判断
#         if prices:
#             mi = prices[0]
#             ma = prices[0]
#             temp = prices[0]
#             isMin = False
#             i = 1
#             while i < len(prices):
#                 v = prices[i]
#                 if isMin and v - temp > ma - mi:
#                     ma = v
#                     mi = temp
#                     temo = False
#                 if v > ma:
#                     ma = v
#                 elif v < mi and v < temp:
#                     temp = v
#                     isMin = True
#                 i += 1
#                 #print(ma, mi, temp)
#             return ma - mi
#         return 0

# print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
# print(Solution().maxProfit([7, 6, 4, 3, 1]))
# print(Solution().maxProfit([4,7,1,2,11]))


"""
Success
Details 
Runtime: 64 ms, faster than 97.71% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 13.8 MB, less than 93.10% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
# 当前大 当前小 
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
#         mini = prices[0]
#         maxi = 0

#         for i in range(1, len(prices)):
#             mini = min(mini, prices[i])
#             maxi = max(maxi, prices[i]-mini)

#         return maxi


"""
Success
Details 
Runtime: 72 ms, faster than 74.67% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 13.7 MB, less than 98.85% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
# max subarray sum 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_cur = 0
        max_so_far = 0
        for i in range(1, len(prices)):
            max_cur += prices[i] - prices[i-1]
            max_cur = max(0, max_cur)
            max_so_far = max(max_so_far, max_cur)

        return max_so_far
