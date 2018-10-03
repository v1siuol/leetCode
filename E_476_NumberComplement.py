"""
149 / 149 test cases passed.
Status: Accepted
Runtime: 45 ms
You are here!
Your runtime beats 47.91% of python submissions.
"""
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = 0
        count = 0
        nTo2 = list(bin(num).replace("0b", ""))

        while nTo2:
            if nTo2.pop() == "0":
                result += 2 ** count
            count += 1
        return result

print(Solution().findComplement(5))