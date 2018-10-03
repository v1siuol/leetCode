"""
315 / 315 test cases passed.
Status: Accepted
Runtime: 66 ms
You are here!
Your runtime beats 83.33% of python submissions.
"""
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        """
        def conv(num):
            i = 0
            while True:
                if str(i) == num:
                    return i
                i += 1
        return str(conv(num1) + conv(num2))
        """
        return str(eval(num1 + "+" + num2))

print(Solution().addStrings("2", "2"))
