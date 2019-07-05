"""
Success
Details 
Runtime: 68 ms, faster than 83.17% of Python online submissions for Flatten Nested List Iterator.
Memory Usage: 17.5 MB, less than 55.86% of Python online submissions for Flatten Nested List Iterator.
"""

from __future__ import annotations 
import collections 
import random 
import heapq 

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # 可用 dict set 提速
        value = [0] * len(words)
        base = ord('a')
        for i, word in enumerate(words):
            for c in word:
                value[i] |= 1 << (ord(c) - base)

        max_product = 0

        for i in range(0, len(words)):
            for j in range(i+1, len(words)):
                if value[i] & value[j] == 0:
                    # no dupl
                    max_product = max(max_product, len(words[i])*len(words[j]))

        return max_product


s = Solution()

ans = s.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"])
exp = 16
print(ans, ans == exp)

ans = s.maxProduct(["a","ab","abc","d","cd","bcd","abcd"])
exp = 4
print(ans, ans == exp)

ans = s.maxProduct(["a","aa","aaa","aaaa"])
exp = 0
print(ans, ans == exp)