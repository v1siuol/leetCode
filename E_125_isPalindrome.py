from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 64 ms, faster than 37.07% of Python3 online submissions for Valid Palindrome.
Memory Usage: 14.4 MB, less than 33.33% of Python3 online submissions for Valid Palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        head = 0
        tail = len(s) - 1

        while head < tail:
            while head < len(s) and not s[head].isalnum():
                head += 1

            while tail >= 0 and  not s[tail].isalnum():
                tail -= 1

            if head >= tail:
                return True

            if s[head].lower() != s[tail].lower():
                return False

            head += 1
            tail -= 1

        return True
