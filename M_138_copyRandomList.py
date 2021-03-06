from __future__ import annotations 
import collections 
import random 
import heapq 


"""
Success
Details 
Runtime: 392 ms, faster than 50.13% of Python online submissions for Copy List with Random Pointer.
Memory Usage: 14.7 MB, less than 22.77% of Python online submissions for Copy List with Random Pointer.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
# class Solution(object):
#     # 只有 py2 能过 py3 全炸
#     """
#     :type head: Node
#     :rtype: Node
#     """
#     def __init__(self):
#         # Dictionary which holds old nodes as keys and new nodes as its values.
#         self.visitedHash = {}

#     def copyRandomList(self, head):

#         if head == None:
#             return None

#         # If we have already processed the current node, then we simply return the cloned version of it.
#         if head in self.visitedHash:
#             return self.visitedHash[head]

#         # create a new node
#         # with the value same as old node.
#         node = Node(head.val, None, None)

#         # Save this value in the hash map. This is needed since there might be
#         # loops during traversal due to randomness of random pointers and this would help us avoid them.
#         self.visitedHash[head] = node

#         # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
#         # Thus we have two independent recursive calls.
#         # Finally we update the next and random pointers for the new node created.
#         node.next = self.copyRandomList(head.next)
#         node.random = self.copyRandomList(head.random)

#         return node



"""
Success
Details 
Runtime: 40 ms, faster than 96.53% of Python3 online submissions for Copy List with Random Pointer.
Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Copy List with Random Pointer.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        # interwined
        curr = head
        while curr:
            cp = Node(curr.val, None, None)
            cp.next = curr.next
            curr.next = cp
            curr = cp.next

        # random
        curr = head
        while curr:
            cp = curr.next
            if curr.random:
                cp.random = curr.random.next
            curr = curr.next.next

        # recover 
        old_curr = head
        ret = new_curr = head.next

        while old_curr:
            old_curr.next = new_curr.next
            if new_curr.next:
                new_curr.next = new_curr.next.next
            old_curr = old_curr.next
            new_curr = new_curr.next

        return ret
