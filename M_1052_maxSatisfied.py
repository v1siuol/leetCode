from __future__ import annotations 
import collections 
import random 
import heapq 


"""
Success
Details 
Runtime: 304 ms, faster than 97.39% of Python3 online submissions for Grumpy Bookstore Owner.
Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Grumpy Bookstore Owner.
"""
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        base = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                base += customers[i]
                customers[i] = 0

        curr = 0
        for i in range(X):
            curr += customers[i]

        max_curr = curr
        for i in range(X, len(customers)):
            curr += customers[i] - customers[i-X]
            max_curr = max(max_curr, curr)

        return max_curr + base
