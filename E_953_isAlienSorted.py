from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 36 ms, faster than 76.76% of Python3 online submissions for Verifying an Alien Dictionary.
Memory Usage: 13.7 MB, less than 5.01% of Python3 online submissions for Verifying an Alien Dictionary.
"""

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i, c in enumerate(order)}
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            for x in range(min(len(word1), len(word2))):
                if word1[x] != word2[x]:
                    if order_index[word1[x]] > order_index[word2[x]]:
                        return False
                    break  # sure small
            else:
                if len(word1) > len(word2):
                    return False 
        return True 

