"""
Success
Details 
Runtime: 60 ms, faster than 66.42% of Python online submissions for Clone Graph.
Memory Usage: 12.7 MB, less than 69.65% of Python online submissions for Clone Graph.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None
        copy_node = Node(node.val, [])
        dct = {node: copy_node}
        dfs(node, dct)
        return copy_node

def dfs(node, dct):
    for neighbor in node.neighbors:
        if neighbor not in dct:
            copy_neighbor = Node(neighbor.val, [])
            dct[neighbor] = copy_neighbor
            dct[node].neighbors.append(copy_neighbor)
            dfs(neighbor, dct)
        else:
            dct[node].neighbors.append(dct[neighbor])
