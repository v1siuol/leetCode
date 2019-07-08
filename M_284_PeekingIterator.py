"""
Success
Details 
Runtime: 12 ms, faster than 98.48% of Python online submissions for Peeking Iterator.
Memory Usage: 12 MB, less than 6.30% of Python online submissions for Peeking Iterator.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 
import pysnooper 


# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.cache = None
        self.has_next = True
        self._helper()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.cache        

    def next(self):
        """
        :rtype: int
        """
        tmp = None
        if self.hasNext():
            tmp = self.cache
            self._helper()
        return tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.has_next
    
    def _helper(self):
        if self.iterator.hasNext():
            self.cache = self.iterator.next()
        else:
            self.cache = None
            self.has_next = False 

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].