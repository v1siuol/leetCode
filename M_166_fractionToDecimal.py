from __future__ import annotations 
import collections 
import random 
import heapq 
import re
import threading


"""
Success
Details 
Runtime: 28 ms, faster than 91.62% of Python3 online submissions for Fraction to Recurring Decimal.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Fraction to Recurring Decimal.
"""
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        sign = '-' if (numerator < 0) ^ (denominator < 0) else ''
        denominator = abs(denominator)
        n, left_n = divmod(abs(numerator), denominator)
        if left_n == 0:
            return sign+str(n)

        res = sign+str(n)+'.'
        idx_store = dict()
        while left_n != 0:
            if left_n in idx_store:
                i = idx_store[left_n]
                res = res[:i]+'('+res[i:]
                res += ')'
                return res
            idx_store[left_n] = len(res)
            n, left_n = divmod(left_n * 10, denominator)
            res += str(n)

        return res
