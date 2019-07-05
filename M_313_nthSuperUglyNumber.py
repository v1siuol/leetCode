"""
Success
Details 
Runtime: 272 ms, faster than 94.98% of Python3 online submissions for Super Ugly Number.
Memory Usage: 17 MB, less than 83.08% of Python3 online submissions for Super Ugly Number.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [0] * n

        min_heap = [(prime, 1, prime) for prime in primes]
        heapq.heapify(min_heap)

        ugly[0] = 1

        for i in range(1, n):
            ugly[i] = min_heap[0][0]
            while min_heap[0][0] == ugly[i]:
                heapq.heapreplace(min_heap, (min_heap[0][2] * ugly[min_heap[0][1]], min_heap[0][1]+1, min_heap[0][2]))

        return ugly[-1]


s = Solution()

print(s.nthSuperUglyNumber(12, [2,7,13,19])) 
