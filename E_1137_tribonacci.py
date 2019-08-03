from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect

class Solution:
    def tribonacci(self, n: int) -> int:
        d = dict()
        d[0] = 0
        d[1] = 1
        d[2] = 1
        return recur(n, d)

def recur(n, dct):
    if n in dct:
        return dct[n]
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    dct[n-1] = recur(n-1, dct)
    dct[n-2] = recur(n-2, dct)
    dct[n-3] = recur(n-3, dct)
    return dct[n-1] + dct[n-2] + dct[n-3]


s = Solution()
print(s.tribonacci(25))
print(s.tribonacci(2))
print(s.tribonacci(4))
