"""
Success
Details 
Runtime: 36 ms, faster than 73.63% of Python3 online submissions for Implement Queue using Stacks.
Memory Usage: 13.1 MB, less than 60.81% of Python3 online submissions for Implement Queue using Stacks.
"""
from __future__ import annotations 
import collections 


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = collections.deque()
        self.output = collections.deque()

        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.output.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.output) == 0:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.input) == 0 and len(self.output) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()