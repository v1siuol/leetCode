from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 36 ms, faster than 80.32% of Python3 online submissions for Divisor Game.
Memory Usage: 13.9 MB, less than 7.64% of Python3 online submissions for Divisor Game.
"""

class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0

