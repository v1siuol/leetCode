from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 388 ms, faster than 80.90% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
Memory Usage: 49.7 MB, less than 8.33% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # bfs O(n) time O(n) space
        queue = collections.deque()
        if not root:
            return root
        
        ret = root
        queue.appendleft(root)
        
        while queue:
            
            next_queue = collections.deque()
            
            while queue:
            
                node = queue.pop()
                if queue:
                    node.next = queue[-1]
                if node.left:
                    next_queue.appendleft(node.left)
                if node.right:
                    next_queue.appendleft(node.right)

            queue = next_queue
            
        return ret
