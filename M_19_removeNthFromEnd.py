"""
Success
Details 
Runtime: 36 ms, faster than 95.01% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.2 MB, less than 30.39% of Python3 online submissions for Remove Nth Node From End of List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dump = ListNode(0)
        dump.next = head

        tail = dump
        count = 0
        while count < n:
            tail = tail.next
            count += 1

        curr = dump
        while tail.next is not None:
            curr = curr.next
            tail = tail.next

        curr.next = curr.next.next

        return dump.next
