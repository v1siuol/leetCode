from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 68 ms, faster than 9.44% of Python3 online submissions for Reverse Nodes in k-Group.
Memory Usage: 14.9 MB, less than 5.88% of Python3 online submissions for Reverse Nodes in k-Group.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 巧妙
        curr = head
        count = 0
        while curr is not None and count < k:
            curr = curr.next
            count += 1

        if count == k:
            curr = self.reverseKGroup(curr, k)
            while count > 0:
                count -= 1
                tmp = head.next
                head.next = curr
                curr = head
                head = tmp
            head = curr

        return head
