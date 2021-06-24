from __future__ import annotations 
import collections 
import random 
import heapq 
import re


"""
Success
Details 
Runtime: 28 ms, faster than 92.28% of Python3 online submissions for Monotone Increasing Digits.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Monotone Increasing Digits.
"""
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        n_str = list(str(N))

        n = len(n_str)
        end = n

        for i in reversed(range(1, n)):
            if n_str[i-1] > n_str[i]:
                end = i
                n_str[i-1] = str(int(n_str[i-1]) - 1)

        n_str[end:] = '9' * (n - end)
        return int(''.join(n_str))
