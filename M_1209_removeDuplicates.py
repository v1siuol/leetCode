from __future__ import annotations 
import collections 
import random 
import heapq 


"""
18 / 18 test cases passed.
Status: Accepted
Runtime: 60 ms
Memory Usage: 14.3 MB
You are here!
Your runtime beats 94.72 % of python3 submissions.
"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['#', 0]]

        for char in s:
            if char != stack[-1][0]:
                stack.append([char, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
                    
        return ''.join(char * count for char, count in stack)
