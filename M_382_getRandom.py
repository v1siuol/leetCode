"""
Success
Details 
Runtime: 236 ms, faster than 40.94% of Python3 online submissions for Linked List Random Node.
Memory Usage: 16.3 MB, less than 70.29% of Python3 online submissions for Linked List Random Node.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        count = 0
        res = None

        curr = self.head
        while curr:
            count += 1
            if random.randrange(count) == 0:
                res = curr.val
            curr = curr.next

        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()