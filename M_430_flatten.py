from __future__ import annotations 
import collections 
import random 
import heapq 
import re
import threading


"""
Success
Details 
Runtime: 36 ms, faster than 97.58% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # dfs recur
        if not head:
        	return head

        dump = Node(None, None, head, None)
        dfs(dump, head)

        dump.next.prev = None
        return dump.next

def dfs(prev, curr):
	if not curr:
		return prev

	prev.next = curr
	curr.prev = prev

	temp_next = curr.next
	tail = dfs(curr, curr.child)
	curr.child = None
	return dfs(tail, temp_next)
