"""
Success
Details 
Runtime: 36 ms, faster than 75.37% of Python3 online submissions for Evaluate Division.
Memory Usage: 13.2 MB, less than 46.67% of Python3 online submissions for Evaluate Division.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        quot = collections.defaultdict(dict)
        for (num, den), val in zip(equations, values):
            quot[num][num] = quot[den][den] = 1.0
            quot[num][den] = val
            quot[den][num] = 1 / val 

        def dfs(start, end, num, used):
            if start in used:
                return 0.0
            if end in quot[start]:
                return quot[start][end] * num
            temp = 0.0
            used.add(start)

            for _next in quot[start]:
                temp = dfs(_next, end, num*quot[start][_next], used)
                if temp != 0.0:
                    break
            used.remove(start)
            return temp

        res = []
        for num, den in queries:
            temp = dfs(num, den, 1.0, set())
            if temp == 0:
                temp = -1.0
            res.append(temp)
        return res



s = Solution()
a = [["a","b"],["b","c"]]
b = [2.0,3.0]
c = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# c = [["a","c"]]
res = s.calcEquation(a, b, c)
exp = [6.0,0.5,-1.0,1.0,-1.0]
print(res, res == exp)
