"""
8 / 8 test cases passed.
Status: Accepted
Runtime: 82 ms
You are here!
Your runtime beats 54.94% of python submissions.
"""
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        count = 1
        result = []
        while count <= n:
            if count % 3 == 0:
                if count % 5 == 0:
                    result.append("FizzBuzz")
                else:
                    result.append("Fizz")
            elif count % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(count))
            count += 1
        return result
