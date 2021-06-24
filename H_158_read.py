from __future__ import annotations 
import collections 
import random 
import heapq 
import re
import threading


"""
Success
Details 
Runtime: 32 ms, faster than 76.04% of Python3 online submissions for Read N Characters Given Read4 II - Call multiple times.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Read N Characters Given Read4 II - Call multiple times.
"""
"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:

    def __init__(self):
        self.buff_counter = 0
        self.buff = [0] * 4
        self.buff_ptr = 0

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        ptr = 0

        while ptr < n:

            if self.buff_ptr == 0:
                self.buff_counter = read4(self.buff)

            if self.buff_counter == 0:
                break

            while ptr < n and self.buff_ptr < self.buff_counter:
                buf[ptr] = self.buff[self.buff_ptr]
                ptr += 1
                self.buff_ptr += 1

            if self.buff_ptr >= self.buff_counter:
                self.buff_ptr = 0

        return ptr

