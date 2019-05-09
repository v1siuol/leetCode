"""
Success
Details 
Runtime: 108 ms, faster than 23.65% of Python online submissions for Shortest Word Distance II.
Memory Usage: 20.3 MB, less than 5.66% of Python online submissions for Shortest Word Distance II.
"""
class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.dct = dict()
        count = 0
        for i, word in enumerate(words):
            if word in self.dct:
                self.dct[word].append(i)
            else:
                self.dct[word] = [i]
            count += 1
        self.count = count

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1 = 0
        i2 = 0
        n1 = len(self.dct[word1])
        n2 = len(self.dct[word2])

        ret = self.count
        # ret = abs(self.dct[word1][i1] - self.dct[word2][i2])
        while i1 < n1 and i2 < n2:
            ret = min(ret, abs(self.dct[word1][i1] - self.dct[word2][i2]))
            if self.dct[word1][i1] < self.dct[word2][i2]:
                i1 += 1
            else:
                i2 += 1

        return ret 



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)


words = ["practice", "makes", "perfect", "coding", "makes"]
obj = WordDistance(words)


word1 = 'coding'
word2 = 'practice'
param_1 = obj.shortest(word1,word2)

print(param_1)


word1 = 'makes'
word2 = 'coding'
param_1 = obj.shortest(word1,word2)

print(param_1)

