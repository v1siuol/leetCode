"""
Success
Details 
Runtime: 68 ms, faster than 41.09% of Python3 online submissions for Min Stack.
Memory Usage: 17.1 MB, less than 6.47% of Python3 online submissions for Min Stack.
"""
from __future__ import annotations 
import collections 


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        
    def push(self, x: int) -> None:
        prev = self.getMin()
        if prev is None or x < prev:
            prev = x
        self.q.append((x, prev))
        
    def pop(self) -> None:
        self.q.pop()

    def top(self) -> int:
        return self.q[-1][0] if self.q else None

    def getMin(self) -> int:
        return self.q[-1][1] if self.q else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
