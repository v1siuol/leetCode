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

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         curr = head
#         prev = None

#         while curr is not None:
#             temp = curr.next  # next 
#             curr.next = prev
#             prev = curr             
#             curr = temp

#         return prev 


"""
Details 
Runtime: 44 ms, faster than 55.81% of Python3 online submissions for Reverse Linked List.
Memory Usage: 19.2 MB, less than 18.18% of Python3 online submissions for Reverse Linked List.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         return recursion(head)

# def recursion(head):
#     if head is None or head.next is None:
#         return head
    
#     new_head = recursion(head.next)
#     head.next.next = head
#     head.next = None
#     return new_head


"""
Success
Details 
Runtime: 36 ms, faster than 45.97% of Python3 online submissions for Reverse Linked List.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Reverse Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         n1 = None
#         n2 = head

#         while n2:
#             temp = n2.next

#             n2.next = n1
#             n1 = n2
#             n2 = temp

#         return n1


"""
Success
Details 
Runtime: 36 ms, faster than 45.97% of Python3 online submissions for Reverse Linked List.
Memory Usage: 17.4 MB, less than 22.73% of Python3 online submissions for Reverse Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return reverse_recur(head)

def reverse_recur(head):
    if head is None or head.next is None:
        return head

    new_head = reverse_recur(head.next)
    head.next.next = head  # 5->4
    head.next = None  # 4->None but next recur
    return new_head
