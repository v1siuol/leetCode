from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 36 ms, faster than 96.08% of Python3 online submissions for Minimum Cost Tree From Leaf Values.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Minimum Cost Tree From Leaf Values.
"""

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        n = len(arr)
        stack = collections.deque([float('inf')])
        for val in arr:
            while stack[-1] <= val:
                mid = stack.pop()
                res += mid * min(stack[-1], val)
            stack.append(val)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res 

