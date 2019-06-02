"""
Success
Details 
Runtime: 32 ms, faster than 96.75% of Python3 online submissions for Reverse Linked List II.
Memory Usage: 13.1 MB, less than 82.68% of Python3 online submissions for Reverse Linked List II.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        _head = ListNode(0)
        _head.next = head
        c = 0
        temp_prev_head = _head
        while c < m-1:
            temp_prev_head = temp_prev_head.next
            c += 1

        curr = temp_prev_head.next
        while c < n-1:
            temp = curr.next
            curr.next = curr.next.next
            temp.next = temp_prev_head.next
            temp_prev_head.next = temp
            c += 1

        return _head.next

