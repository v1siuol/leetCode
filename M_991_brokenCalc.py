from __future__ import annotations 
import collections 
import random 
import heapq 


"""
Success
Details 
Runtime: 36 ms, faster than 52.03% of Python3 online submissions for Broken Calculator.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Broken Calculator.
"""
# 反着来
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        count = 0
        while X < Y:
            count += Y % 2 + 1
            Y = (Y + 1) // 2
        return count + X - Y
