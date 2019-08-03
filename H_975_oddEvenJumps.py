from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 388 ms, faster than 48.05% of Python3 online submissions for Odd Even Jump.
Memory Usage: 18.6 MB, less than 19.30% of Python3 online submissions for Odd Even Jump.
"""

class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        next_higher = [0] * n
        next_lower = [0] * n

        stack = collections.deque()
        for a, idx in sorted([a, idx] for idx, a in enumerate(A)):
            while stack and stack[-1] < idx:
                next_higher[stack.pop()] = idx
            stack.append(idx)
        stack = collections.deque()
        for a, idx in sorted([-a, idx] for idx, a in enumerate(A)):
            while stack and stack[-1] < idx:
                next_lower[stack.pop()] = idx
            stack.append(idx)

        higher = [0] * n
        lower = [0] * n
        higher[-1] = lower[-1] = 1
        for i in range(n-1)[::-1]:
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]

        return sum(higher)
