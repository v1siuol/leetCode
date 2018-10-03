"""
Author  => v1siuol
Date    => 2017.01.25
You are here!
Your runtime beats 51.08% of python submissions.
"""
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        result = 0
        xTo2 = list(bin(x).replace("0b", ""))
        yTo2 = list(bin(y).replace("0b", ""))

        while True:
            if xTo2.pop() != yTo2.pop():
                result += 1
            if not xTo2:
                # xTo2 is empty
                result += yTo2.count("1")
                return result
            if not yTo2:
                result += xTo2.count("1")
                return result
        return -1


    # 思路：位运算 单元自带二进制 / 计算多少1可以用 n & n-1去除最右的1
    def tinghao(self, x, y):
        c = 0 
        n = x ^ y
        while (n > 0):
            c += 1
            n &= n - 1
        return c

        # return bin(x^y).count('1')



a = Solution()
print(a.hammingDistance(1,4))
print(a.tinghao(1,4))
