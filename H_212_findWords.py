"""
Success
Details 
Runtime: 372 ms, faster than 56.80% of Python3 online submissions for Word Search II.
Memory Usage: 36.2 MB, less than 25.66% of Python3 online submissions for Word Search II.
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

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie()
        node = trie.root 
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board, node, i, j, '', res)

        return res 

def dfs(board, node, i, j, path, res):
    if node.is_word:
        res.append(path)
        node.is_word = False 
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return 
    tmp = board[i][j]
    node = node.children.get(tmp)
    if not node:
        return 
    board[i][j] = '#'
    dfs(board, node, i+1, j, path+tmp, res)
    dfs(board, node, i-1, j, path+tmp, res)
    dfs(board, node, i, j+1, path+tmp, res)
    dfs(board, node, i, j-1, path+tmp, res)
    board[i][j] = tmp 


s = Solution()
print(s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))

print(s.findWords([["a","a"]],["aaa"]))
