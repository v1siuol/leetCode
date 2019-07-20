from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 48 ms, faster than 87.11% of Python3 online submissions for Longest Valid Parentheses.
Memory Usage: 13.6 MB, less than 56.46% of Python3 online submissions for Longest Valid Parentheses.
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        ret = 0
        stack.append(-1)

        for idx, char in enumerate(s):
            if char == '(':
                stack.append(idx)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(idx)
                else:
                    ret = max(ret, idx-stack[-1])
        return ret 

