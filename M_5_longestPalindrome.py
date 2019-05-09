"""
Success
Details 
Runtime: 776 ms, faster than 81.78% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 12.4 MB, less than 87.35% of Python3 online submissions for Longest Palindromic Substring.
"""

"""
目前 O(n^2) 长度处理迷了 
最优 O(n) Manacher's algorithm 
"""

class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':

        def bi_expand(left, right):
            ret_length = 0
            while left >= 0 and right < n and s[left] == s[right]:
                ret_length = right - left

                left -= 1
                right += 1
            return ret_length

        n = len(s)
        max_length = -1
        ret_str = ''
        for i in range(n):
            length_with_center = bi_expand(i, i)  # more on 2
            length_without_center = bi_expand(i, i+1)  # more on 1  

            # print(i, length_with_center, length_without_center, max_length)

            if length_with_center > max_length:
                max_length = length_with_center
                ret_str = s[i-length_with_center//2:i+length_with_center//2+1]

            if length_without_center > max_length:
                max_length = length_without_center
                ret_str = s[i-length_without_center//2:i+length_without_center//2+2]

        return ret_str


        

sol = Solution()
print(sol.longestPalindrome('babad'))
print(sol.longestPalindrome('cbbd'))
print(sol.longestPalindrome(''))
print(sol.longestPalindrome('a'))
print(sol.longestPalindrome('ac'))
print(sol.longestPalindrome('tattarrattat'))
