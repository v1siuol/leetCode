"""
Success
Details 
Runtime: 92 ms, faster than 18.15% of Python3 online submissions for Reverse Vowels of a String.
Memory Usage: 15.8 MB, less than 5.08% of Python3 online submissions for Reverse Vowels of a String.
"""
class Solution:
    def reverseVowels(self, s: 'str') -> 'str':
        # 双指针
        vowels = {'o', 'e', 'u', 'i', 'a', 'O', 'E', 'U', 'I', 'A'}
        i = 0
        j = len(s) - 1
        rec = dict()
        while i < j:
            while i < len(s) and s[i] not in vowels:
                i += 1
            while j >= 0 and s[j] not in vowels:
                j -= 1
            if i >= j:
                break
            else:
                # print(s[i], s[j])
                # s[i], s[j] = s[j], s[i]
                rec[i] = j
                rec[j] = i

            i += 1
            j -= 1

        ret = ''
        i = 0
        while i < len(s):
            if i not in rec:
                ret += s[i]
            else:
                ret += s[rec[i]]

            i += 1

        return ret




s = Solution()
# print(s.reverseVowels("hello"))
# print(s.reverseVowels("a"))
# print(s.reverseVowels("leetcode"))
# print(s.reverseVowels("aA"))
# print(s.reverseVowels("a.b,."))
print(s.reverseVowels(",."))

