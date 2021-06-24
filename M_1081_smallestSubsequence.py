from __future__ import annotations 
import collections 
import random 
import heapq 


"""
Success
Details 
Runtime: 36 ms, faster than 19.90% of Python3 online submissions for Smallest Subsequence of Distinct Characters.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Smallest Subsequence of Distinct Characters.
"""
# class Solution:
#     def smallestSubsequence(self, text: str) -> str:
#         last = {char: idx for idx, char in enumerate(text)}
#         stack = []
#         for i, c in enumerate(text):
#             if c in stack:
#                 continue
#             while stack and stack[-1] > c and last[stack[-1]] > i:
#                 stack.pop()
#             stack.append(c)
#         return ''.join(stack)


"""
Success
Details 
Runtime: 40 ms, faster than 16.33% of Python3 online submissions for Smallest Subsequence of Distinct Characters.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Smallest Subsequence of Distinct Characters.
"""
class Solution:
    def smallestSubsequence(self, text: str) -> str:
        last = {char: idx for idx, char in enumerate(text)}
        stack = []
        used = set()
        for i, c in enumerate(text):
            if c in used:
                continue
            while stack and stack[-1] > c and last[stack[-1]] > i:
                used.remove(stack.pop())
            stack.append(c)
            used.add(c)
        return ''.join(stack)
