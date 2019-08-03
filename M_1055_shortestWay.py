from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 56 ms, faster than 56.14% of Python3 online submissions for Shortest Way to Form String.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Shortest Way to Form String.
"""

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        t_idx = 0
        ret = 0
        while t_idx < len(target):
            prev_t_idx = t_idx

            for s in source:
                if s == target[t_idx]:
                    t_idx += 1
                if t_idx == len(target):
                    break

            if t_idx == prev_t_idx:
                return -1 
            ret += 1  # add 1 cmb 

        return ret 

