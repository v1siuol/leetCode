from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 216 ms, faster than 28.82% of Python3 online submissions for Max Stack.
Memory Usage: 16 MB, less than 25.00% of Python3 online submissions for Max Stack.
"""

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = collections.deque()
        self.max_stack = collections.deque()

    def push(self, x: int) -> None:
        self.push_helper(x)

    def pop(self) -> int:
        self.max_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1]

    def popMax(self) -> int:
        # find the max
        max_val = self.max_stack[-1]
        temp_stack = collections.deque()

        while self.stack[-1] != max_val:
            temp_stack.append(self.stack.pop())
            self.max_stack.pop()

        self.stack.pop()
        self.max_stack.pop()

        while temp_stack:
            self.push_helper(temp_stack.pop())

        return max_val

    def push_helper(self, x):
        temp_max = x if len(self.max_stack) == 0 else max(self.max_stack[-1], x)
        self.stack.append(x)
        self.max_stack.append(temp_max)


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()