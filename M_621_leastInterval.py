from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 476 ms, faster than 12.16% of Python3 online submissions for Task Scheduler.
Memory Usage: 14.1 MB, less than 5.08% of Python3 online submissions for Task Scheduler.
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # greedy calc 
        counter = [0] * 26
        m = 0
        max_count = 0
        for task in tasks:
            idx = ord(task) - ord('A')
            counter[idx] += 1
            if m == counter[idx]:
                max_count += 1
            elif m < counter[idx]:
                m = counter[idx]
                max_count = 1 

        part_count = m - 1 
        part_length = n - (max_count - 1)
        empty = part_count * part_length
        avail = len(tasks) - m * max_count
        idles = max(0, empty-avail)
        return len(tasks) + idles
