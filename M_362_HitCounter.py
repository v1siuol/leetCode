"""
Success
Details 
Runtime: 32 ms, faster than 93.13% of Python3 online submissions for Design Hit Counter.
Memory Usage: 13.4 MB, less than 5.02% of Python3 online submissions for Design Hit Counter.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 
import pysnooper 

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.window = [(0,0)] * 300
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        idx = timestamp % 300
        t, h = self.window[idx]
        self.window[idx] = (timestamp, 1) if timestamp != t else (t, h+1)
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        return sum((h for t, h in self.window if timestamp - t < 300))


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)