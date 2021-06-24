from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 72 ms, faster than 86.34% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 16.3 MB, less than 82.26% of Python3 online submissions for Merge k Sorted Lists.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         head = curr = ListNode(None)
#         h = [(l.val, idx) for idx, l in enumerate(lists) if l]
#         heapq.heapify(h)

#         while h:
#             val, idx = heapq.heappop(h)
#             curr.next = ListNode(val)
#             curr = curr.next
#             node = lists[idx] = lists[idx].next
#             if node:
#                 heapq.heappush(h, (node.val, idx))

#         return head.next


"""
Success
Details 
Runtime: 112 ms, faster than 77.92% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.2 MB, less than 27.27% of Python3 online submissions for Merge k Sorted Lists.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # heap!! 
        head = curr = ListNode(None)
        lst = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(lst)

        while lst:
            node_val, node_idx = heapq.heappop(lst)
            curr.next = ListNode(node_val)
            curr = curr.next
            node = lists[node_idx] = lists[node_idx].next
            if node:
                heapq.heappush(lst, (node.val, node_idx))

        return head.next
