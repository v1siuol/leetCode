"""
31 / 31 test cases passed.
Status: Accepted
Runtime: 1235 ms
You are here!
Your runtime beats 65.21% of python submissions.
"""
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def d(x, y):
            return (y[1] - x[1]) ** 2 + (y[0] - x[0]) ** 2

        def c(x):
            t = 1
            for i in range(2, x-1):
                t *= i
            q = t * (x-1) * x
            return q / 2 / t

        re = 0
        for i in points[:]:
            dic = dict()
            for j in points[:]:

                t = d(i, j)
                if t in dic:
                    dic[t] += 1
                else:
                    dic[t] = 1
            #print(dic)
            for i in dic.values():
                if i > 1:
                    re += c(i)
                    #re += i
        return int(re) * 2
