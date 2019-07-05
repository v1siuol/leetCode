"""
Success
Details 
Runtime: 100 ms, faster than 81.72% of Python3 online submissions for Insert Delete GetRandom O(1) - Duplicates allowed.
Memory Usage: 17.1 MB, less than 61.95% of Python3 online submissions for Insert Delete GetRandom O(1) - Duplicates allowed.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.pos[val].add(len(self.nums))
        self.nums.append(val)
        return len(self.pos[val]) == 1  


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if self.pos[val]:
            last = self.nums[-1]
            idx = self.pos[val].pop()
            self.nums[idx] = last
            self.pos[last].add(idx)
            self.pos[last].discard(len(self.nums)-1)
            self.nums.pop()
            return True 
        return False 

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()