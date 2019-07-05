"""
Success
Details 
Runtime: 88 ms, faster than 65.06% of Python3 online submissions for Mini Parser.
Memory Usage: 16.5 MB, less than 59.41% of Python3 online submissions for Mini Parser.
"""
from __future__ import annotations 
import collections 


# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))

        curr = None
        stack = collections.deque()
        l = 0

        for r in range(len(s)):
            ch = s[r]
            if ch == '[':
                if curr:
                    stack.append(curr)
                curr = NestedInteger()
                l = r + 1 
            elif ch == ']':
                num = s[l:r]
                if num:
                    curr.add(NestedInteger(int(num)))
                if stack:
                    head = stack.pop()
                    head.add(curr)
                    curr = head
                l = r + 1
            elif ch == ',':
                if s[r-1] != ']':
                    num = s[l:r]
                    curr.add(NestedInteger(int(num)))
                l = r + 1

        return curr
