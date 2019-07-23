from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect



"""
Success
Details 
Runtime: 244 ms, faster than 16.53% of Python3 online submissions for Design HashMap.
Memory Usage: 17 MB, less than 33.70% of Python3 online submissions for Design HashMap.
"""

class Node(object):
    """docstring for Node"""
    def __init__(self, key, value):
        # super(Node, self).__init__()
        self.pair = (key, value)
        self.next = None
        

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000
        self.h = [None] * self.m
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.m
        if self.h[idx] is None:
            self.h[idx] = Node(key, value)
        else:
            curr = self.h[idx]
            while True:
                if curr.pair[0] == key:
                    curr.pair = (key, value)
                    return
                if curr.next is None:
                    break
                curr = curr.next
            curr.next = Node(key, value)


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % self.m
        curr = self.h[idx]
        while curr:
            if curr.pair[0] == key:
                return curr.pair[1]
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = key % self.m
        prev = curr = self.h[idx]
        if curr is None:
            return 
        elif curr.pair[0] == key:
            self.h[idx] = curr.next
        else:
            curr = curr.next
            while curr:
                if curr.pair[0] == key:
                    prev.next = curr.next
                    break
                else:
                    prev, curr = curr, curr.next 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
