"""
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
