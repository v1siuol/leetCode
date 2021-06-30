from __future__ import annotations
import collections
import random
import heapq

"""
Success
Details 
Runtime: 144 ms, faster than 16.24% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
Memory Usage: 20.6 MB, less than 16.38% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
Areas of improvement: Fast&slow to find mid; Add short circuiting;
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def recur(head, tail):
            if head == tail:
                return None

            slow = head
            fast = head
            while fast != tail and fast.next != tail:
                slow = slow.next
                fast = fast.next.next
            root = TreeNode(slow.val)
            root.left = recur(head, slow)
            root.right = recur(slow.next, tail)
            return root

        return recur(head, None)

