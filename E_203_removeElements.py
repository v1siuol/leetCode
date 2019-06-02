"""
Success
Details 
Runtime: 68 ms, faster than 98.35% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 16.5 MB, less than 43.79% of Python3 online submissions for Remove Linked List Elements.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dump = ListNode(0)
        dump.next = head

        curr = dump
        while curr.next is not None:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dump.next
