from __future__ import annotations
import collections
import random
import heapq

"""
Success
Details 
Runtime: 56 ms, faster than 92.89% of Python3 online submissions for Populating Next Right Pointers in Each Node.
Memory Usage: 15.6 MB, less than 69.71% of Python3 online submissions for Populating Next Right Pointers in Each Node.
Areas of improvement:
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = curr = root
        prev = next_level = None
        while curr and curr.left:
            if not prev:
                next_level = curr.left
            else:
                prev.next = curr.left
            curr.left.next = curr.right
            if curr.next:
                prev = curr.right
                curr = curr.next
            else:
                prev = None
                curr = next_level

        return head
