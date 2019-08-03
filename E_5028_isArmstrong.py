from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


class Solution:
    def isArmstrong(self, N: int) -> bool:
        if N < 0:
            return False
        res = 0
        k = len(str(N))
        n = N
        while n != 0:
            last = n % 10
            n //= 10
            res += last ** k
        return res == N

