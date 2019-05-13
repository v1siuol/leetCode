"""
Success
Details 
Runtime: 224 ms, faster than 48.16% of Python3 online submissions for Reverse Words in a String II.
Memory Usage: 17.6 MB, less than 5.36% of Python3 online submissions for Reverse Words in a String II.
"""
class Solution:
    def reverseWords(self, str: 'List[str]') -> 'None':
        """
        Do not return anything, modify str in-place instead.
        """
        i = 0
        j = len(str) - 1
        while i < j:
            str[i], str[j] = str[j], str[i]
            i += 1
            j -= 1

        i = 0
        j = 0
        while i < len(str) and j < len(str):
            while i < j or str[i] == ' ':
                i += 1

            while j < i or j < len(str) and str[j] != ' ':
                j += 1

            # swap str i - j-1
            p = i
            q = j-1
            while p < q:
                str[p], str[q] = str[q], str[p]
                p += 1
                q -= 1


s = Solution()
i = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
s.reverseWords(i)
print(i)

