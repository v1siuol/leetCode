"""
Success
Details 
Runtime: 44 ms, faster than 47.75% of Python online submissions for Shortest Word Distance III.
Memory Usage: 16.4 MB, less than 5.55% of Python online submissions for Shortest Word Distance III.
"""
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dis = len(words)
        loc1 = -1
        loc2 = -1

        for i, word in enumerate(words):
            if word == word1 and word == word2:
                if loc1 == -1:
                    loc1 = i
                else:
                    dis = min(dis, i-loc1)
                    loc1 = i

            elif word1 == word:
                loc1 = i
                if loc2 != -1:
                    dis = min(dis, abs(loc1-loc2))
            elif word2 == word:
                loc2 = i
                if loc1 != -1:
                    dis = min(dis, abs(loc1-loc2))

        return dis




s = Solution()


words = ["practice", "makes", "perfect", "coding", "makes"]



word1 = 'makes'
word2 = 'coding'

print(s.shortestWordDistance(words, word1, word2))

word1 = 'makes'
word2 = 'makes'

print(s.shortestWordDistance(words, word1, word2))
