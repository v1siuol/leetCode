"""
Success
Details 
Runtime: 996 ms, faster than 5.07% of Python3 online submissions for Add and Search Word - Data structure design.
Memory Usage: 132.7 MB, less than 5.01% of Python3 online submissions for Add and Search Word - Data structure design.
"""

from __future__ import annotations 
import collections 
import random 
import heapq 
import pysnooper 

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True 

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(node, word):
            if not word:
                if node.isWord:
                    self.res = True 
                return 
            if word[0] == '.':
                for n in node.children.values():
                    dfs(n, word[1:])
            else:
                node = node.children[word[0]]
                if not node:
                    return 
                dfs(node, word[1:])

        node = self.root
        self.res = False
        dfs(node, word)
        return self.res 
        
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False 


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

