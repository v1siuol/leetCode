"""
Success
Details 
Runtime: 88 ms, faster than 79.60% of Python3 online submissions for Logger Rate Limiter.
Memory Usage: 19 MB, less than 60.51% of Python3 online submissions for Logger Rate Limiter.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 
import pysnooper 

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if timestamp < self.log.get(message, 0):
            return False
        self.log[message] = timestamp + 10
        return True 



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)