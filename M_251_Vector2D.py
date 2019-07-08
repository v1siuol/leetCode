"""
Success
Details 
Runtime: 72 ms, faster than 96.37% of Python3 online submissions for Flatten 2D Vector.
Memory Usage: 18.6 MB, less than 60.38% of Python3 online submissions for Flatten 2D Vector.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 
import pysnooper 

class Vector2D:

    def __init__(self, v: List[List[int]]):
        def iterator():
            for l in v:
                for i in l:
                    self.size -= 1
                    yield i 
        self.size = sum(len(line) for line in v)
        self.iterator = iterator()

    def next(self) -> int:
        return next(self.iterator)
        

    def hasNext(self) -> bool:
        return self.size > 0 
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()