from __future__ import annotations 
import collections 
import random 
import heapq 
import math


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        seen = dict()
        count = 0
        for d in dominoes:
            t = tuple(sorted(d))
            if t in seen:
                count += seen[t]
                seen[t] += 1
            else:
                seen[t] = 1

        return count 


s = Solution()
dominoes = [[1,2],[2,1],[3,4],[5,6]]
print(s.numEquivDominoPairs(dominoes))


dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
print(s.numEquivDominoPairs(dominoes))

