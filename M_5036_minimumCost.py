from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


class Solution:
    def minimumCost(self, N: int, conections: List[List[int]]) -> int:
        # greedy 
        if len(conections) < N - 1:
            return -1
        if N == 1:
            return 0

        res = 0
        pq = []
        for (p1, p2, cost) in conections:
            heapq.heappush(pq, (cost, p1, p2))

        avail = set(range(1, N+1))

        n = N
        roots = [i for i in range(N)]

        # while avail:
        while n != 1:
            if len(pq) == 0:
                # cant reach 
                return -1
            cost, p1, p2 = heapq.heappop(pq)
            # if p1 in avail or p2 in avail:
            #     # print(cost)
                
            #     if p1 in avail:
            #         avail.remove(p1)
            #     if p2 in avail:
            #         avail.remove(p2)

            x = find(roots, p1-1)
            y = find(roots, p2-1)
            if x != y:
                roots[x] = y  # union 
                res += cost
                n -= 1
            # print(x, y, roots)

            # print(avail)

        # # check 
        # n = N
        # roots = [i for i in range(N)]
        # for p1, p2, _ in conections:
        #     x = find(roots, p1-1)
        #     y = find(roots, p2-1)
        #     if x != y:
        #         roots[x] = y  # union 
        #         n -= 1
        #     print(x, y, roots)
        # if n > 1:
        #     return -1

        return res 


def find(roots, id):
    while roots[id] != id:
        roots[id] = roots[roots[id]]
        id = roots[id]
    return id



s = Solution()

N = 3
conections = [[1,2,5],[1,3,6],[2,3,1]]
print(s.minimumCost(N, conections))

N = 4
conections = [[1,2,3],[3,4,4]]
print(s.minimumCost(N, conections))

N = 5
conections = [[1,2,3],[3,4,4], [4,5,4], [3,5,4]]
print(s.minimumCost(N, conections))

N = 1
conections = []
print(s.minimumCost(N, conections))


N = 7
conections = [[2,1,87129],[3,1,14707],[4,2,34505],[5,1,71766],[6,5,2615],[7,2,37352]]
print(s.minimumCost(N, conections))

# 24xxxx
