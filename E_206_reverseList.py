"""
Success
Details 
Runtime: 28 ms, faster than 99.96% of Python3 online submissions for Reverse Linked List.
Memory Usage: 14.5 MB, less than 48.28% of Python3 online submissions for Reverse Linked List.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None

        while curr is not None:
            temp = curr.next  # next 
            curr.next = prev
            prev = curr             
            curr = temp

        return prev 
