"""
Success
Details 
Runtime: 44 ms, faster than 96.95% of Python3 online submissions for Odd Even Linked List.
Memory Usage: 15.1 MB, less than 28.96% of Python3 online submissions for Odd Even Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)

        while head is not None:
            odd.next = head
            even.next = head.next

            odd = odd.next
            even = even.next

            head = even.next if even is not None else None

        odd.next = dummy2.next
        return dummy1.next

