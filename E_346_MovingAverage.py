"""
Success
Details 
Runtime: 56 ms, faster than 94.34% of Python3 online submissions for Moving Average from Data Stream.
Memory Usage: 16.6 MB, less than 7.95% of Python3 online submissions for Moving Average from Data Stream.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 
import pysnooper 

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.n = 0
        self.replace = 0
        self.s = 0
        self.window = [0] * size 

    def next(self, val: int) -> float:
        if self.n < self.size:
            self.n += 1
        self.s -= self.window[self.replace]
        self.s += val
        self.window[self.replace] = val
        self.replace = (self.replace + 1) % self.size

        return self.s / self.n

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)