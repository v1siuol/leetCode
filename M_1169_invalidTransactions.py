from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 68 ms, faster than 98.47% of Python3 online submissions for Invalid Transactions.
Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Invalid Transactions.
"""
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # O(n^2) O(n)
        ret = set()
        records = collections.defaultdict(list)
        for t in transactions:
            name, time, amount, city = t.split(',')
            if int(amount) > 1000:
                ret.add(t)
            records[name].append( (int(time), city, t) )
            
        for val in records.values():
            val.sort()
            for i in range(len(val)):
                for j in range(i+1, len(val)):
                    if val[i][0] >= val[j][0]-60:
                        if val[i][1] != val[j][1]:
                            ret.add(val[i][2])
                            ret.add(val[j][2])
                    else:
                        break
                
        return list(ret)
