"""
39 / 39 test cases passed.
Status: Accepted
Runtime: 92 ms
You are here!
Your runtime beats 2.69 % of python3 submissions.
"""
class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """

        result = 0
        # for index in range(len(ops)):
        for item in ops[:]:
            index = ops.index(item)
            if '+' == ops[index]:
                ops[index] = (int(ops[index-1])+int(ops[index-2]))
                result += ops[index]
            elif 'D' == ops[index]:
                ops[index] = int(ops[index-1]) * 2
                result += ops[index]
            elif 'C' == ops[index]:
                result -= int(ops.pop(index-1))
                ops.pop(index-1)
            else:
                result += int(ops[index])
        return result
