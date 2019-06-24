"""
Success
Details 
Runtime: 32 ms, faster than 94.46% of Python3 online submissions for Nested List Weight Sum II.
Memory Usage: 13.5 MB, less than 37.62% of Python3 online submissions for Nested List Weight Sum II.
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
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        unweighted = 0
        weighted = 0
        while nestedList:
            temp = collections.deque()
            for item in nestedList:
                if item.isInteger():
                    unweighted += item.getInteger()
                else:
                    for y in item.getList():
                        temp.append(y)
            weighted += unweighted
            nestedList = temp 

        return weighted

