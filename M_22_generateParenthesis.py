from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 40 ms, faster than 80.48% of Python3 online submissions for Generate Parentheses.
Memory Usage: 13.4 MB, less than 44.75% of Python3 online submissions for Generate Parentheses.
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        backtracking('', 0, 0, n, ret)
        return ret 

def backtracking(path, left, right, n, ret):
    if len(path) == n * 2:
        ret.append(path)
        return 
    if left < n:
        backtracking(path+'(', left+1, right, n, ret)
    if right < left:
        backtracking(path+')', left, right+1, n, ret)
