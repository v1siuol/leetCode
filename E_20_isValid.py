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

# class Solution:
#     def isValid(self, s: str) -> bool:
#         # stack
#         stack = collections.deque()
#         match = {'(':')', '{':'}', '[':']'}
#         for char in s:
#             if char in {'(', '{', '['}:
#                 stack.append(char)
#             else:
#                 if not stack or char != match[stack.pop()]:
#                     return False 
#         return len(stack) == 0 


"""
Success
Details 
Runtime: 40 ms, faster than 46.83% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.8 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.
"""

# class Solution:
#     def isValid(self, s: str) -> bool:
#         # stack
#         match = {'(': ')', '{': '}', '[': ']'}
#         stack = collections.deque()
#         for token in s:
#             if token in match:
#                 stack.append(token)
#             else:
#                 if len(stack) == 0:
#                     return False
#                 left_token = stack.pop()
#                 if token != match[left_token]:
#                     return False
                
#         return len(stack) == 0 


"""
Success
Details 
Runtime: 28 ms, faster than 95.80% of Python3 online submissions for Valid Parentheses.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        # stack 
        # O(n) time O(n) space
        stack = []
        prev_match = {'(': ')', '{':'}', '[':']'}
        for char in s:
            if char in {'(', '{', '['}:
                stack.append(char)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if prev_match[prev] != char:
                    return False
        return len(stack) == 0