from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 36 ms, faster than 97.90% of Python3 online submissions for Two City Scheduling.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Two City Scheduling.
"""
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # O(n log n) O(n)
        total_cost = 0
        n = len(costs)
        diff = [(c[1]-c[0], i) for i, c in enumerate(costs)]
        diff.sort(key=lambda x: -abs(x[0]))
        
        a_count = 0
        b_count = 0
        for dif, idx in diff:
            if a_count == n // 2:
                total_cost += costs[idx][1]
                continue
                # b_count += 1
            if b_count == n // 2:
                total_cost += costs[idx][0]
                continue
                # a_count += 1
            if dif > 0:
                a_count += 1
                total_cost += costs[idx][0]
            elif dif < 0:
                total_cost += costs[idx][1]
                b_count += 1
            else:
                if a_count < b_count:
                    a_count += 1
                    total_cost += costs[idx][0]
                else:
                    total_cost += costs[idx][1]
                    b_count += 1
                    
        return total_cost


# 可优化 greedy 
