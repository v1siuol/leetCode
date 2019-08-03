from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Runtime: 520 ms
Memory Usage: 17.3 MB
You are here! 
Your runtime beats 89.32 % of python3 submissions.
You are here! 
Your memory usage beats 9.35 % of python3 submissions.
"""

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = [0] * len(T)
        top = -1
        ret = [0] * len(T)
        for i in range(len(T)):
            while top > -1 and T[i] > T[stack[top]]:
                idx = stack[top]
                top -= 1
                ret[idx] = i - idx
            top += 1
            stack[top] = i
        return ret 
