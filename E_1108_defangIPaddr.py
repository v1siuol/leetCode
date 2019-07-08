
from __future__ import annotations 
import collections 
import random 
import heapq 
import pysnooper 

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.'))



s = Solution()
address = "1.1.1.1"
print(s.defangIPaddr(address))

address = "255.100.50.0"
print(s.defangIPaddr(address))
