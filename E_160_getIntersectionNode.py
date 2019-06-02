"""
Success
Details 
Runtime: 196 ms, faster than 90.77% of Python online submissions for Intersection of Two Linked Lists.
Memory Usage: 41.8 MB, less than 63.55% of Python online submissions for Intersection of Two Linked Lists.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curr_a = headA
        curr_b = headB
        tail_a = None
        tail_b = None

        if curr_a is None or curr_b is None:
            return None

        while True:
            if curr_a is curr_b:
                return curr_a
            else:
                if curr_a.next is not None:
                    curr_a = curr_a.next
                else:
                    tail_a = curr_a
                    curr_a = headB

                if curr_b.next is not None:
                    curr_b = curr_b.next
                else:
                    tail_b = curr_b
                    curr_b = headA

                if tail_a is not None and tail_b is not None and tail_a is not tail_b:
                    return None
