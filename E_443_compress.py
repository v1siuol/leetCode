from __future__ import annotations 
import collections 
import random 
import heapq 
import re
import threading


"""
Success
Details 
Runtime: 56 ms, faster than 94.67% of Python3 online submissions for String Compression.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for String Compression.
"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        index_ans = 0
        i = 0
        while i < len(chars):
            curr_char = chars[i]
            count = 0
            while i < len(chars) and curr_char == chars[i]:
                i += 1
                count += 1
            chars[index_ans] = curr_char
            index_ans += 1
            if count > 1:
                for count_char in str(count):
                    chars[index_ans] = count_char
                    index_ans += 1
        return index_ans
