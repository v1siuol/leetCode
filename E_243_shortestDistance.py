"""
Success
Details 
Runtime: 44 ms, faster than 53.71% of Python online submissions for Shortest Word Distance.
Memory Usage: 16.6 MB, less than 6.35% of Python online submissions for Shortest Word Distance.
"""
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        loc1 = -1
        loc2 = -1
        dis = len(words) # imp

        for i, word in enumerate(words):
            if word == word1:
                loc1 = i
                if loc2 != -1:
                    dis = min(dis, abs(loc1-loc2))
            elif word == word2:
                loc2 = i
                if loc1 != -1:
                    dis = min(dis, abs(loc1-loc2))

        return dis


s = Solution()


words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = 'coding'
word2 = 'practice'

print(s.shortestDistance(words, word1, word2))


word1 = 'makes'
word2 = 'coding'

print(s.shortestDistance(words, word1, word2))

