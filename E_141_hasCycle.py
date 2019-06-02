"""
Success
Details 
Runtime: 32 ms, faster than 98.91% of Python online submissions for Linked List Cycle.
Memory Usage: 18 MB, less than 93.48% of Python online submissions for Linked List Cycle.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False 

        slow = head
        fast = head.next

        while slow is not fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

