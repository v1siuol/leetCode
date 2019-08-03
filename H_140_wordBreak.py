from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 56 ms, faster than 62.63% of Python3 online submissions for Word Break II.
Memory Usage: 13.8 MB, less than 5.48% of Python3 online submissions for Word Break II.
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return recur(s, wordDict, dict())

def recur(s, wordDict, memo):
    if s in memo:
        return memo.get(s)

    res = []
    if len(s) == 0:
        res.append('')
        return res

    for word in wordDict:
        if s.startswith(word):
            sublist = recur(s[len(word):], wordDict, memo)
            for sub in sublist:
                res.append(word + ('' if sub=='' else ' ') + sub)
    memo[s] = res
    return res


