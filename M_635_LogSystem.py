from __future__ import annotations 
import collections 
import random 
import heapq 

"""
Success
Details 
Runtime: 56 ms, faster than 93.04% of Python3 online submissions for Design Log Storage System.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Design Log Storage System.
"""
class LogSystem:

    def __init__(self):
        self.store = []
        self.granularity = {'Year': 4, 'Month': 7, 'Day': 10, 'Hour': 13, 'Minute': 16, 'Second': 19}

    def put(self, id: int, timestamp: str) -> None:
    	# O(1)
        self.store.append( (timestamp, id) )

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
    	# O(n)
        idx = self.granularity[gra]
        start = s[:idx]
        end = e[:idx]

        return [id for timestamp, id in self.store if start <= timestamp[:idx] <= end]


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)