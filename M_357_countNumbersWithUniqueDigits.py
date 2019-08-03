from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 32 ms, faster than 85.94% of Python3 online submissions for Count Numbers with Unique Digits.
Memory Usage: 13.8 MB, less than 6.67% of Python3 online submissions for Count Numbers with Unique Digits.
"""

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        res = 10
        avail = 9
        uniq = 9
        while avail > 0 and n > 1:
            n -= 1
            uniq *= avail
            res += uniq
            avail -= 1
        return res 
