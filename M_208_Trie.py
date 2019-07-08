"""
Success
Details 
Runtime: 156 ms, faster than 68.13% of Python3 online submissions for Implement Trie (Prefix Tree).
Memory Usage: 29.9 MB, less than 26.08% of Python3 online submissions for Implement Trie (Prefix Tree).
"""
from __future__ import annotations 
import collections 
import random 
import heapq 
import pysnooper 

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False 

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for letter in word:
            curr = curr.children[letter]
        curr.is_word = True 

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for letter in word:
            curr = curr.children.get(letter)
            if curr is None:
                return False
        return curr.is_word 

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for letter in prefix:
            curr = curr.children.get(letter)
            if curr is None:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
