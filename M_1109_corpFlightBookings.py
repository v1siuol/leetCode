
from __future__ import annotations 
import collections 
import random 
import heapq 
import pysnooper 

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ps = [0] * n
        for i, j, k in bookings:
            ps[i-1] += k
            if j != n:
                ps[j] -= k

        s = 0
        res = []
        for i in ps:
            s += i
            res.append(s)
        return res 


        
s = Solution()
bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
print(s.corpFlightBookings(bookings, n))
