"""
Success
Details 
Runtime: 148 ms, faster than 34.94% of Python3 online submissions for LRU Cache.
Memory Usage: 22.1 MB, less than 21.03% of Python3 online submissions for LRU Cache.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 

class Node():
    def __init__(self):
        self.key = 0 
        self.value = 0 
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = dict()
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node is None:
            return -1 
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if node is None:
            new = Node()
            new.key = key
            new.value = value 

            self.cache[key] = new
            self._add_node(new)

            self.size += 1

            if self.size > self.capacity:
                # pop the tail 
                tail = self._pop_tail()
                self.cache.pop(tail.key)
                self.size -= 1
        else:
            # update and move 
            node.value = value
            self._move_to_head(node)


    def _add_node(self, node):
        # right after dump head 
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node 
        self.head.next = node 

    def _remove_node(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev 

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res 

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)