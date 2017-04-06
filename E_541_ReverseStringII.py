"""
60 / 60 test cases passed.
Status: Accepted
Runtime: 55 ms
"""
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        i = 0
        re = ""
        while i < len(s):
            while i + 2 * k < len(s):
                #print(i, k)
                re += s[i + k - 1:i:-1]
                re += s[i]
                #while k >= 0:
                #    re += s[i + k-1]
                #    k -= 1
                #print(k)
                re += s[i+k:i + 2 * k]
                #print(re)
                i += 2 * k
                #print(i)
                #print("test")
            if i + k > len(s):
                re += s[len(s)-1:i:-1]
                re += s[i]
                break
            else:
                re += s[i+k-1:i:-1]
                re += s[i]
                i += k
                re += s[i:]
                break
        return re
