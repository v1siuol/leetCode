"""
Success
Details 
Runtime: 44 ms, faster than 95.21% of Python3 online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 13.2 MB, less than 43.94% of Python3 online submissions for Remove Duplicates from Sorted List II.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dump = ListNode(None)
        dump.next = head 

        prev = dump

        while prev.next is not None and prev.next.next is not None:
            curr_val = prev.next.val
            curr_node = prev.next.next

            if curr_val == curr_node.val:
                while curr_node is not None and curr_val == curr_node.val:
                    curr_node = curr_node.next
                prev.next = curr_node
            else:
                prev = prev.next

        return dump.next
