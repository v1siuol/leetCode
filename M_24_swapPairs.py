"""
Success
Details 
Runtime: 48 ms, faster than 18.66% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 13.3 MB, less than 19.61% of Python3 online submissions for Swap Nodes in Pairs.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # new head 
        if head is None or head.next is None:
            return head

        curr1 = head
        curr2 = head.next

        curr3 = curr2.next

        curr1.next = curr3
        curr2.next = curr1
        _head = curr2

        prev = curr1

        while prev.next is not None and prev.next.next is not None:

            curr1 = prev.next
            curr2 = prev.next.next
            curr3 = curr2.next
            curr1.next = curr3
            curr2.next = curr1
            prev.next = curr2
            prev = curr1

        return _head
