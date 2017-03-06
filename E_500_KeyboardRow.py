"""
22 / 22 test cases passed.
Status: Accepted
Runtime: 59 ms
You are here!
Your runtime beats 13.43% of python submissions.
"""
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        q = "qwertyuiopQWERTYUIOP"
        a = "asdfghjklASDFGHJKL"
        z = "zxcvbnmZXCVBNM"
        re = []
        for word in words:
            print(word)
            c = 1
            re.append(word)
            print(word[0])
            if word[0] in q:
                while c < len(word):
                    if word[c] not in q:
                        re.remove(word)
                        break
                    c += 1
            elif word[0] in a:
                print(word)
                while c < len(word):
                    if word[c] not in a:
                        re.remove(word)
                        break
                    c += 1
            elif word[0] in z:
                while c < len(word):
                    if word[c] not in z:
                        re.remove(word)
                        break
                    c += 1
        return re
