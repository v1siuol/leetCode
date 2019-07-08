"""
Success
Details 
Runtime: 60 ms, faster than 19.91% of Python online submissions for Zigzag Iterator.
Memory Usage: 12.2 MB, less than 5.14% of Python online submissions for Zigzag Iterator.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 
import pysnooper 

class ZigzagIterator(object):
    # pop 0 败笔 on 

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.q = collections.deque()
        if v1: 
            self.q.append(v1)
        if v2:
            self.q.append(v2)

    def next(self):
        """
        :rtype: int
        """
        v = self.q.popleft()
        ret = v.pop(0)
        if v:
            self.q.append(v)
        return ret 


    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.q) > 0 


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())