"""
Success
Details 
Runtime: 96 ms, faster than 88.98% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 16.9 MB, less than 45.26% of Python3 online submissions for Insert Delete GetRandom O(1).
"""
from __future__ import annotations 
import collections 
import random 
import heapq 


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = dict()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.pos:
            self.pos[val] = len(self.nums)
            self.nums.append(val)
            return True 
        return False 

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.pos:
            idx = self.pos[val]
            last = self.nums[-1]
            self.nums[idx] = last
            self.pos[last] = idx
            self.nums.pop()
            self.pos.pop(val)
            return True 
        return False 
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[random.randrange(len(self.nums))]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
