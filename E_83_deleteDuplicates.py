"""
Success
Details 
Runtime: 40 ms, faster than 98.84% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 13.2 MB, less than 25.02% of Python3 online submissions for Remove Duplicates from Sorted List.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        if curr is None:
            return head
        _next = curr.next

        while _next is not None:
            if curr.val == _next.val:
                _next = _next.next
                curr.next = _next
            else:
                curr = _next
                _next = _next.next

        return head
