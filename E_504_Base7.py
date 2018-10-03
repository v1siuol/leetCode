"""
241 / 241 test cases passed.
Status: Accepted
Runtime: 42 ms
You are here!
Your runtime beats 73.34% of python submissions.
"""
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        re = []
        temp = abs(num)
        while temp > 6:
            re.append(str(temp % 7))
            temp //= 7
        re.append(str(temp))
        if num < 0:
            re.append("-")
        re.reverse()
        return "".join(re)

print(Solution().convertToBase7(100))
print(Solution().convertToBase7(-7))
print(Solution().convertToBase7(-8))
