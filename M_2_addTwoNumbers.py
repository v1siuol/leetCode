from __future__ import annotations 
import collections 
import random 
import heapq 


"""
divmod
单链表
1563 / 1563 test cases passed.
Status: Accepted
Runtime: 68 ms
You are here! 
Your runtime beats 95.48 % of python submissions.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         root = curr = ListNode(0)
#         curry = 0
#         while l1 or l2 or curry:
#             value = 0
#             if curry:
#                 value += curry
#                 curry = 0
#             if l1:
#                 value += l1.val
#                 l1 = l1.next
#             if l2:
#                 value += l2.val
#                 l2 = l2.next
#             curry, value = divmod(value, 10)  # //, %

#             curr.next = ListNode(value)
#             curr = curr.next

#         return root.next


"""
Success
Details 
Runtime: 88 ms, faster than 16.63% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14 MB, less than 5.67% of Python3 online submissions for Add Two Numbers.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # O(n) O(1) 还可以减少 assign var
        head = curr = ListNode(None)  # dump 
        
        carry = 0
        while l1 or l2 or carry:
            n1 = 0
            n2 = 0
            if l1 is not None:
                n1 = l1.val
                l1 = l1.next
            if l2 is not None:
                n2 = l2.val
                l2 = l2.next
            
            total = n1 + n2 + carry
            s = total % 10 
            carry = total // 10
            
            node = ListNode(s)
            curr.next = node
            curr = node 
        
        return head.next
