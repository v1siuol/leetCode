"""
Success
Details 
Runtime: 40 ms, faster than 86.51% of Python3 online submissions for Count and Say.
Memory Usage: 13.2 MB, less than 5.11% of Python3 online submissions for Count and Say.
"""


class Solution:
    def countAndSay(self, n: 'int') -> 'str':
        ret = '1'
        for i in range(1, n):
            j = 1
            curr_count = 1
            new = ''
            while j < len(ret):
                if ret[j] == ret[j-1]:
                    curr_count += 1
                else:
                    new += str(curr_count) + ret[j-1]
                    curr_count = 1
                j += 1
            ret = new + str(curr_count) + ret[j-1]

        return ret


s = Solution()
print(s.countAndSay(1))
print(s.countAndSay(4))


