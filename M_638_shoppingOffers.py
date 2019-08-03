from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 84 ms, faster than 73.81% of Python3 online submissions for Shopping Offers.
Memory Usage: 13.9 MB, less than 32.84% of Python3 online submissions for Shopping Offers.
"""

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        memo = dict()
        return recur(needs, price, special, memo, 0)

def recur(curr_needs, price, special, memo, special_idx):
    curr_min = 0
    s = str(curr_needs)
    if s in memo:
        return memo[s]

    for i in range(len(curr_needs)):
        curr_min += curr_needs[i] * price[i]

    for i in range(special_idx, len(special)):
        temp = curr_needs[:]
        for j in range(len(curr_needs)):
            if curr_needs[j] < special[i][j]:
                temp = []
                break
            temp[j] = curr_needs[j] - special[i][j]

        if len(temp) > 0:
            curr_min = min(curr_min, special[i][-1]+recur(temp, price, special, memo, i))

    memo[s] = curr_min
    return curr_min
