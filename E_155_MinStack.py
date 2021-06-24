from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 68 ms, faster than 41.09% of Python3 online submissions for Min Stack.
Memory Usage: 17.1 MB, less than 6.47% of Python3 online submissions for Min Stack.
"""

# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.q = []
        
#     def push(self, x: int) -> None:
#         prev = self.getMin()
#         if prev is None or x < prev:
#             prev = x
#         self.q.append((x, prev))
        
#     def pop(self) -> None:
#         self.q.pop()

#     def top(self) -> int:
#         return self.q[-1][0] if self.q else None

#     def getMin(self) -> int:
#         return self.q[-1][1] if self.q else None


# # Your MinStack object will be instantiated and called as such:
# # obj = MinStack()
# # obj.push(x)
# # obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.getMin()


"""
Success
Details 
Runtime: 52 ms, faster than 99.69% of Python3 online submissions for Min Stack.
Memory Usage: 16.3 MB, less than 100.00% of Python3 online submissions for Min Stack.
"""
# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         # O(1) time O(n) space
#         self.min_stack = []
#         self.stack = []
        
#     def push(self, x: int) -> None:
#         self.stack.append(x)
#         if len(self.min_stack) == 0 or x <= self.min_stack[-1]:
#             self.min_stack.append(x)

#     def pop(self) -> None:
#         pop_val = self.stack.pop()
#         if pop_val == self.min_stack[-1]:
#             self.min_stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


"""
Success
Details 
Runtime: 52 ms, faster than 99.69% of Python3 online submissions for Min Stack.
Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Min Stack.
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.curr_min = float('inf')
        self.stack = []

    def push(self, x: int) -> None:
        # 把之前的min append进去
        if x <= self.curr_min:
            self.stack.append(self.curr_min)
            self.curr_min = x
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.curr_min:
            self.curr_min = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # stack empty ? 
        return self.curr_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()