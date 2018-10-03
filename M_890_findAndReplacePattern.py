class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        stand = self.helper(pattern)
        a = map(self.helper, words) 
        ws = [i for i in a]

        res = []
        i = 0
        while i < len(words):
            if ws[i] == stand:
                res.append(words[i])
            i += 1
        return res


        
    def helper(self, strs):
        i = 0
        dc = dict()
        res = ''
        while i < len(strs):
            if strs[i] not in dc:
                dc[strs[i]] = i

            res+=str(dc[strs[i]])
            i += 1

        return res

print(Solution().findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))
