"""
31 / 31 test cases passed.
Status: Accepted
Runtime: 155 ms
You are here!
Your runtime beats 11.97 % of python3 submissions.
"""
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        results = []
        is_result = True
        for i in range(left, right+1):
            st = str(i)
            for wei in range(len(st)):
                if st[wei] == '0':
                    is_result = False
                    break
                if st[wei] != '1':
                    if i % int(st[wei]) != 0:
                        is_result = False
            if is_result:
                results.append(i)
            is_result = True
        return results


print(Solution().selfDividingNumbers(1, 22))
