from __future__ import annotations 
import collections 
import random 
import heapq 


"""
Success
Details 
Runtime: 96 ms, faster than 88.98% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 16.9 MB, less than 45.26% of Python3 online submissions for Insert Delete GetRandom O(1).
"""

# class RandomizedSet:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.nums = []
#         self.pos = dict()

#     def insert(self, val: int) -> bool:
#         """
#         Inserts a value to the set. Returns true if the set did not already contain the specified element.
#         """
#         if val not in self.pos:
#             self.pos[val] = len(self.nums)
#             self.nums.append(val)
#             return True 
#         return False 

#     def remove(self, val: int) -> bool:
#         """
#         Removes a value from the set. Returns true if the set contained the specified element.
#         """
#         if val in self.pos:
#             idx = self.pos[val]
#             last = self.nums[-1]
#             self.nums[idx] = last
#             self.pos[last] = idx
#             self.nums.pop()
#             self.pos.pop(val)
#             return True 
#         return False 
        

#     def getRandom(self) -> int:
#         """
#         Get a random element from the set.
#         """
#         return self.nums[random.randrange(len(self.nums))]
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()



"""
Success
Details 
Runtime: 88 ms, faster than 99.81% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 16.9 MB, less than 29.17% of Python3 online submissions for Insert Delete GetRandom O(1).
"""
# dict val idx list val 
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val2idx = dict()
        self.vals = []
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        # 插最后 
        if val in self.val2idx:
            return False
        self.val2idx[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # 找到换最后一个
        if val not in self.val2idx:
            return False
        last_val = self.vals[-1]
        idx = self.val2idx[val]
        self.vals[idx] = last_val
        self.val2idx[last_val] = idx
        self.vals.pop()
        self.val2idx.pop(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # O(1)
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()