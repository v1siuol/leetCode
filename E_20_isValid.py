from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 32 ms, faster than 91.42% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.1 MB, less than 81.59% of Python3 online submissions for Valid Parentheses.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # stack
        stack = collections.deque()
        match = {'(':')', '{':'}', '[':']'}
        for char in s:
            if char in {'(', '{', '['}:
                stack.append(char)
            else:
                if not stack or char != match[stack.pop()]:
                    return False 
        return len(stack) == 0 