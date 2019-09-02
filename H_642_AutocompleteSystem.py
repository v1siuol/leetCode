from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 664 ms, faster than 75.85% of Python3 online submissions for Design Search Autocomplete System.
Memory Usage: 21.8 MB, less than 33.33% of Python3 online submissions for Design Search Autocomplete System.
"""

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.count = collections.defaultdict(int)

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.prefix = ''
        self.node = self.root

        for i in range(len(sentences)):
            self.add(sentences[i], times[i])

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.add(self.prefix, 1)
            self.prefix = ''
            self.node = self.root
            return []
        self.prefix += c
        self.node = self.node.children[c]

        pq = []
        for key, val in self.node.count.items():
            heapq.heappush(pq, (-val, key))

        ret = []
        for _ in range(3):
            if not pq:
                break
            ret.append(heapq.heappop(pq)[1])
        return ret

    def add(self, sentence, time):
        curr = self.root
        for char in sentence:
            curr = curr.children[char]
            curr.count[sentence] += time

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)