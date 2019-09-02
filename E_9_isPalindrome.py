from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 80 ms, faster than 35.91% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.2 MB, less than 5.82% of Python3 online submissions for Palindrome Number.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev = 0
        tmp = x
        while tmp != 0:
            rev = rev * 10 + tmp % 10
            tmp //= 10
        return rev == x

# 折半 
