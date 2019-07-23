from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 836 ms, faster than 27.65% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.8 MB, less than 5.13% of Python3 online submissions for Fibonacci Number.
"""

class Solution:
    def fib(self, N: int) -> int:
        return fib_cur(N)

def fib_cur(n):
    if n <= 1:
        return n
    return fib_cur(n-1) + fib_cur(n-2)

# 换位会快些 
