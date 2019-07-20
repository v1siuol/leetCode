"""
Success
Details 
Runtime: 80 ms, faster than 70.88% of Python3 online submissions for Design Phone Directory.
Memory Usage: 16.6 MB, less than 51.85% of Python3 online submissions for Design Phone Directory.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.used = set()
        self.avail = collections.deque()
        for i in range(maxNumbers):
            self.avail.append(i)

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if self.avail:
            n = self.avail.pop()
            self.used.add(n)
            return n
        return -1 

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return number not in self.used

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if number in self.used:
            self.used.remove(number)
            self.avail.append(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)