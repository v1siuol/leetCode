from __future__ import annotations 
import collections 
import random 
import heapq 


"""
Success
Details 
Runtime: 148 ms, faster than 34.94% of Python3 online submissions for LRU Cache.
Memory Usage: 22.1 MB, less than 21.03% of Python3 online submissions for LRU Cache.
"""

# class Node():
#     def __init__(self):
#         self.key = 0 
#         self.value = 0 
#         self.prev = None
#         self.next = None

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.size = 0
#         self.cache = dict()
#         self.head = Node()
#         self.tail = Node()

#         self.head.next = self.tail
#         self.tail.prev = self.head
        

#     def get(self, key: int) -> int:
#         node = self.cache.get(key)
#         if node is None:
#             return -1 
#         self._move_to_head(node)
#         return node.value

#     def put(self, key: int, value: int) -> None:
#         node = self.cache.get(key)

#         if node is None:
#             new = Node()
#             new.key = key
#             new.value = value 

#             self.cache[key] = new
#             self._add_node(new)

#             self.size += 1

#             if self.size > self.capacity:
#                 # pop the tail 
#                 tail = self._pop_tail()
#                 self.cache.pop(tail.key)
#                 self.size -= 1
#         else:
#             # update and move 
#             node.value = value
#             self._move_to_head(node)


#     def _add_node(self, node):
#         # right after dump head 
#         node.prev = self.head
#         node.next = self.head.next
#         self.head.next.prev = node 
#         self.head.next = node 

#     def _remove_node(self, node):
#         prev = node.prev
#         new = node.next

#         prev.next = new
#         new.prev = prev 

#     def _move_to_head(self, node):
#         self._remove_node(node)
#         self._add_node(node)

#     def _pop_tail(self):
#         res = self.tail.prev
#         self._remove_node(res)
#         return res 

# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)


"""
Success
Details 
Runtime: 252 ms, faster than 32.82% of Python3 online submissions for LRU Cache.
Memory Usage: 23.5 MB, less than 6.06% of Python3 online submissions for LRU Cache.
"""

# class Node:
#     def __init__(self):
#         self.key = 0
#         self.value = 0
#         self.next = None
#         self.prev = None

# # 双链表? 
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cache = dict()
#         self.capacity = capacity
#         self.head = Node()
#         self.tail = Node()
#         self.size = 0
#         self.head.next = self.tail
#         self.tail.prev = self.head


#     def get(self, key: int) -> int:
#         node = self.cache.get(key)
#         if node is None:
#             return -1
#         self._move_to_head(node)
#         return node.value

#     def put(self, key: int, value: int) -> None:
#         node = self.cache.get(key)
#         if node is not None:
#             # update 
#             node.value = value
#             self._move_to_head(node)
#         else:
#             # add
#             node = Node()
#             node.key = key
#             node.value = value
#             self.cache[key] = node

#             self._add_node(node)
#             self.size += 1
#             if self.size > self.capacity:
#                 # remove 
#                 real_tail = self.tail.prev
#                 self.cache.pop(real_tail.key)
#                 self._remove_node(real_tail)
#                 self.size -= 1

#     def _move_to_head(self, node):
#         self._remove_node(node)
#         self._add_node(node)

#     def _remove_node(self, node):
#         node.prev.next = node.next
#         node.next.prev = node.prev

#     def _add_node(self, node):
#         node.prev = self.head
#         node.next = self.head.next

#         self.head.next.prev = node
#         self.head.next = node


# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)


"""
Success
Details 
Runtime: 224 ms, faster than 37.43% of Python3 online submissions for LRU Cache.
Memory Usage: 22.4 MB, less than 6.06% of Python3 online submissions for LRU Cache.
"""
class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

# double linked list + dict 
class LRUCache:

    def __init__(self, capacity: int):
        self.dict = dict()
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self._move_to_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.val = value
            self._move_to_head(node)
        else:
            node = self._add_to_head(key, value)
            self.dict[key] = node
            if len(self.dict) > self.capacity:
                removed_node = self.tail.prev
                self.dict.pop(removed_node.key)
                self._remove_node(removed_node)

    def _remove_node(self, removed_node):
        removed_node.prev.next = removed_node.next
        removed_node.next.prev = removed_node.prev

    def _add_to_head(self, key, value):
        node = Node(key, value)
        prev_head = self.head.next
        self.head.next = node
        node.next = prev_head
        node.prev = self.head
        prev_head.prev = node
        return node

    def _move_to_head(self, node):
        self._remove_node(node)
        node = self._add_to_head(node.key, node.val)
        self.dict[node.key] = node 

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)