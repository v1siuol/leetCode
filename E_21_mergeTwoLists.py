from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 40 ms, faster than 95.07% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.3 MB, less than 15.66% of Python3 online submissions for Merge Two Sorted Lists.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         # 剩余可用优化 linkedlist 头部可以优化 
#         if l1 is None:
#             return l2
#         if l2 is None:
#             return l1
#         dump = ListNode(0)

#         prev = dump

#         l1_node = l1
#         l2_node = l2

#         while l1_node is not None and l2_node is not None:
#             if l1_node.val < l2_node.val:
#                 prev.next = l1_node
#                 l1_node = l1_node.next
#                 prev = prev.next
#             elif l1_node.val > l2_node.val:
#                 prev.next = l2_node
#                 l2_node = l2_node.next           
#                 prev = prev.next
#             else:
#                 prev.next = l1_node
#                 l1_node = l1_node.next
#                 prev = prev.next
#                 prev.next = l2_node
#                 l2_node = l2_node.next           
#                 prev = prev.next

#         # left 
#         while l1_node is not None:
#             prev.next = l1_node
#             l1_node = l1_node.next
#             prev = prev.next

#         while l2_node is not None:
#             prev.next = l2_node
#             l2_node = l2_node.next
#             prev = prev.next          

#         return dump.next


#         # l1_node = l1
#         # l2_node = l2
#         # new_head = l1 # empty 
#         # new_tail = l1

#         # if l1 is None:
#         #     return l2
#         # if l2 is None:
#         #     return l1

#         # while l1_node is not None and l2_node is not None:
#         #     l1_node = l1_node.next
#         #     new_tail.next = l2_node
#         #     new_tail = new_tail.next

#         #     l2_node = l2_node.next
#         #     new_tail.next = l1_node
#         #     new_tail = new_tail.next

#         # # while l1_node is not None:
#         # #     new_tail.next = l1_node
#         # #     new_tail = new_tail.next


#         # return new_head


"""
Success
Details 
Runtime: 44 ms, faster than 64.10% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.9 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = dump = ListNode(None)

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                curr = l1
                l1 = l1.next
            else:
                curr.next = l2
                curr = l2
                l2 = l2.next

        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return dump.next
