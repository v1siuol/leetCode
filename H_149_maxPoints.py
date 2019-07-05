"""
Success
Details 
Runtime: 88 ms, faster than 57.64% of Python3 online submissions for Max Points on a Line.
Memory Usage: 13.3 MB, less than 54.32% of Python3 online submissions for Max Points on a Line.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)

        dct = collections.defaultdict(dict)
        max_count = 0
        for i in range(len(points)):
            dct.clear()
            dup = 0
            temp = 0
            for j in range(i+1, len(points)):
                x = points[j][0] - points[i][0]
                y = points[j][1] - points[i][1]
                if x == 0 and y == 0:
                    dup += 1
                    continue 
                g = gcd(x, y)
                if g != 0:
                    x /= g
                    y /= g 
                if y in dct[x]:
                    dct[x][y] += 1
                else:
                    dct[x][y] = 1

                temp = max(temp, dct[x][y])
            max_count = max(max_count, temp+dup+1)

        return max_count

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x%y)


s = Solution()

a = [[1,1],[2,2],[3,3]]
res = s.maxPoints(a)
exp = 3
print(res, res == exp)

a = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
res = s.maxPoints(a)
exp = 4
print(res, res == exp)
