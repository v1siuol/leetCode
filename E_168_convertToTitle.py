"""
Success
Details 
Runtime: 36 ms, faster than 84.24% of Python3 online submissions for Excel Sheet Column Title.
Memory Usage: 13.1 MB, less than 72.63% of Python3 online submissions for Excel Sheet Column Title.
"""

class Solution:
    def convertToTitle(self, n: 'int') -> 'str':
        # to 26 base 
        n2l = {1: 'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8: 'H', 9:'I',
                10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q',
                18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}

        shang = (n-1) // 26
        yushu = (n-1) % 26
        ret = n2l[yushu+1]
        while shang != 0:
            yushu = (shang-1) % 26
            ret = n2l[yushu+1] + ret
            shang = (shang-1) // 26

        return ret


s = Solution()

print(s.convertToTitle(1))
print(s.convertToTitle(28))
print(s.convertToTitle(701))
print(s.convertToTitle(52))
