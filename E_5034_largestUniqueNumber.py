from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect



class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        counter = collections.Counter(A)
        lst = [a for a in counter if counter[a] == 1]
        return max(lst) if lst else -1
