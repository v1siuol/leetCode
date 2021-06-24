from __future__ import annotations 
import collections 
import random 
import heapq 
import re


"""
Success
Details 
Runtime: 348 ms, faster than 95.91% of Python3 online submissions for Concatenated Words.
Memory Usage: 15.8 MB, less than 100.00% of Python3 online submissions for Concatenated Words.
"""
# class Solution:
#     def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
#         words.sort(key=lambda w: len(w))
#         prev_words = set()
#         res = []

#         for word in words:
#             if is_concat(word, prev_words):
#                 res.append(word)
#             prev_words.add( word )
#         return res

# def is_concat(word, prev_words):
#     if word in prev_words:
#         return True
#     for i in range(1, len(word)):
#         if word[:i] in prev_words and is_concat(word[i:], prev_words):
#             return True
#     return False



"""
Success
Details 
Runtime: 1568 ms, faster than 9.27% of Python3 online submissions for Concatenated Words.
Memory Usage: 15.9 MB, less than 100.00% of Python3 online submissions for Concatenated Words.
"""
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=lambda w: len(w))
        prev_words = set()
        res = []

        for word in words:
            if is_concat(word, prev_words):
                res.append(word)
            prev_words.add( word )
        return res

def is_concat(s: str, words: List[str]) -> bool:
    if s == '':
        return False
    dp = [True]
    for end in range(1, len(s)+1):
        dp.append(any(dp[j] and s[j:end] in words for j in range(end)))
    return dp[-1]
