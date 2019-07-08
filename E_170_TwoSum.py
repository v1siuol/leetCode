"""
Success
Details 
Runtime: 272 ms, faster than 77.68% of Python3 online submissions for Two Sum III - Data structure design.
Memory Usage: 18.9 MB, less than 7.21% of Python3 online submissions for Two Sum III - Data structure design.
"""

from __future__ import annotations 
import collections 
import random 
import heapq 

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = collections.defaultdict(int)


    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.s[number] += 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for val in self.s:
            if (value - val in self.s) and (value - val != val or self.s[val] > 1):
                return True 
        return False  


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)