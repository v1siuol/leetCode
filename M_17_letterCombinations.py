from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 32 ms, faster than 91.18% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 13.1 MB, less than 83.57% of Python3 online submissions for Letter Combinations of a Phone Number.
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dct = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], 
               '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        if digits == '':
            return []

        ret = ['']
        for d in digits:
            ret = [curr+char for curr in ret for char in dct[d]]
        return ret 
