"""
Success
Details 
Runtime: 44 ms, faster than 19.90% of Python3 online submissions for Strobogrammatic Number.
Memory Usage: 13.4 MB, less than 5.10% of Python3 online submissions for Strobogrammatic Number.
"""

class Solution:
    def isStrobogrammatic(self, num: 'str') -> 'bool':
        # 双指针会简单些  
        upside_down = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        i = 0
        if len(num) < 2:
            return num == '' or num[0] in {'0', '1', '8'}

        while i < (len(num)+1) // 2:
            if not (num[i] in upside_down and num[-i-1] in upside_down[num[i]]):
                return False
            i += 1
        return True


s = Solution()
print(s.isStrobogrammatic('69'))
print(s.isStrobogrammatic('88'))
print(s.isStrobogrammatic('962'))
print(s.isStrobogrammatic('10'))
print(s.isStrobogrammatic('2'))
print(s.isStrobogrammatic('1'))
print(s.isStrobogrammatic('6'))
print(s.isStrobogrammatic('659'))
