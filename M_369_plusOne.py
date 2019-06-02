"""
Success
Details 
Runtime: 36 ms, faster than 90.03% of Python3 online submissions for Plus One Linked List.
Memory Usage: 13.2 MB, less than 28.29% of Python3 online submissions for Plus One Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dump = ListNode(1)
        dump.next = head

        before9_last_bit = head
        end_bit = head

        while end_bit.next is not None:
            if end_bit.next.val != 9:
                before9_last_bit = end_bit.next
            end_bit = end_bit.next

        if end_bit.val != 9:
            end_bit.val += 1
            return dump.next
        else:
            if before9_last_bit.val == 9:
                before9_last_bit.val = 0
                while before9_last_bit.next is not None:
                    before9_last_bit.next.val = 0
                    before9_last_bit = before9_last_bit.next

                return dump
            else:
                before9_last_bit.val += 1
                while before9_last_bit.next is not None:
                    before9_last_bit.next.val = 0
                    before9_last_bit = before9_last_bit.next
                return dump.next

