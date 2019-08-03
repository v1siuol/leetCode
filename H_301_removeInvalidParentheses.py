from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 24 ms, faster than 100.00% of Python3 online submissions for Remove Invalid Parentheses.
Memory Usage: 13.9 MB, less than 17.44% of Python3 online submissions for Remove Invalid Parentheses.
"""

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # diao 
        ret = []
        remove(s, ret, 0, 0, '()')
        return ret 

def remove(s, ret, last_i, last_j, par):
    stack = 0
    for i in range(last_i, len(s)):
        if s[i] == par[0]:
            stack += 1
        elif s[i] == par[1]:
            stack -= 1
        if stack >= 0:
            continue 
        # more ) 
        for j in range(last_j, i+1):
            if s[j] == par[1] and (j == last_j or s[j-1] != par[1]):
                remove(s[:j]+s[j+1:], ret, i, j, par)
        return 

    rev_s = s[::-1]
    if par[0] == '(':
        remove(rev_s, ret, 0, 0, ')(')
    else:
        ret.append(rev_s)
