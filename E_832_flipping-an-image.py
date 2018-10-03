"""
82 / 82 test cases passed.
Status: Accepted
Runtime: 36 ms
You are here! 
Your runtime beats 90.61 % of python submissions.
"""
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [0 for _ in A]
        m = 0

        while m < len(A):

            temp = []
            arr = A[m][:]
            arr.reverse()

            for n in arr:
                if n == 0:
                    temp.append(1)
                else:
                    temp.append(0)

            res[m] = (temp[:])
            m += 1

        return res
