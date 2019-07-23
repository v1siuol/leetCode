from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect

"""
Success
Details 
Runtime: 732 ms, faster than 5.05% of Python3 online submissions for Time Based Key-Value Store.
Memory Usage: 62.7 MB, less than 5.15% of Python3 online submissions for Time Based Key-Value Store.
"""

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = collections.defaultdict(list)
        self.values = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect(self.times[key], timestamp)
        # 在要插入的位置前面 
        return self.values[key][i-1] if i else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

