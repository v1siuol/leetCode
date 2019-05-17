"""
Success
Details 
Runtime: 476 ms, faster than 5.11% of Python3 online submissions for Rearrange String k Distance Apart.
Memory Usage: 13.4 MB, less than 94.86% of Python3 online submissions for Rearrange String k Distance Apart.
"""

class Solution:
    def rearrangeString(self, s: 'str', k: 'int') -> 'str':
        # 2 array
        char_count = [0] * 26
        next_valid_pos = [0] * 26
        curr_pos = 0
        ord_a = ord('a')
        ret = ''
        for char in s:
            char_count[ord(char)-ord_a] += 1

        for i in range(len(s)):
            candidate = get_most_char(char_count, next_valid_pos, i)
            if candidate == -1:
                return ''
            else:
                char_count[candidate] -= 1
                next_valid_pos[candidate] += k
                ret += chr(candidate + ord_a)
        return ret


def get_most_char(char_count, next_valid_pos, curr_pos):
    # print(char_count, next_valid_pos)
    curr_max = float('-inf')
    pos = -1
    for i in range(26):
        if char_count[i] > 0 and char_count[i] > curr_max and next_valid_pos[i] <= curr_pos:
            curr_max = char_count[i]
            pos = i
    return pos





s = Solution()
print(s.rearrangeString("aabbcc", 3))
print(s.rearrangeString("aaabc", 3))
print(s.rearrangeString("aaadbbcc", 2))


