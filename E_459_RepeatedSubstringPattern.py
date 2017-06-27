"""
107 / 107 test cases passed.
Status: Accepted
Runtime: 246 ms
You are here!
Your runtime beats 26.80 % of python submissions.
"""
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        begin = s[0]
        index = 1
        count = 1
        while index < len(s):
            #print(s[index], begin)
            if s[index] == begin:

                #you keneng
                ding = index
                if ding + index <= len(s):
                    #print(begin, ding, index)
                    while s[0:ding] == s[index:index+ding]:
                        #print(index, s[0:ding], s[index:index + ding])

                        index += ding
                        #print("s",index)
                        if index == len(s):
                            return True
                index = ding
            index += 1
        return False

#print(Solution().repeatedSubstringPattern("abab"))
#print(Solution().repeatedSubstringPattern("aba"))
print(Solution().repeatedSubstringPattern("abcabcabcabc"))
print(Solution().repeatedSubstringPattern("abaababaab"))

