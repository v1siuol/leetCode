from __future__ import annotations 
import collections 
import random 
import heapq 
import re


"""
Success
Details 
Runtime: 2400 ms, faster than 87.72% of Python3 online submissions for Critical Connections in a Network.
Memory Usage: 82.5 MB, less than 100.00% of Python3 online submissions for Critical Connections in a Network.
"""
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = make_graph(connections)
        connections = set(map(tuple, (map(sorted, connections))))
        rank = [-2] * n

        def dfs(node, depth):
            if rank[node] >= 0:
                return rank[node]
            rank[node] = depth
            min_back_depth = n
            for neighbor in graph[node]:
                if rank[neighbor] == depth - 1:
                    continue 
                back_depth = dfs(neighbor, depth+1)
                if back_depth <= depth:
                    connections.discard(tuple(sorted((node, neighbor))))
                min_back_depth = min(min_back_depth, back_depth)
            # rank[node] = n
            return min_back_depth

        dfs(0, 0)
        return list(connections)


def make_graph(connections):
    graph = collections.defaultdict(list)
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)
    return graph
