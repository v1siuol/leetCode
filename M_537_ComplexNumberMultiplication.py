"""
55 / 55 test cases passed.
Status: Accepted
Runtime: 38 ms
You are here!
Your runtime beats 85.56 % of python submissions.
"""
class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #print(a.split("+")[1][:-1])
        a1 = a.split("+")[0]
        a2 = a.split("+")[1][:-1]
        b1 = b.split("+")[0]
        b2 = b.split("+")[1][:-1]
        #print(eval(a1+"*"+b1))
        #print(eval(a1+ "*"+b2))
        #print(eval(a2+ "*"+b1))

        r1 = eval(a1 + "*" + b1) - eval(a2+ "*"+b2)
        r2 = eval(a1+ "*"+b2) + eval(a2+ "*"+b1)
        #print(r1, r2)
        #eval(a.split("+")[0], "*", a.split("+")[0])
        return str(r1)+"+"+str(r2)+"i"


print(Solution().complexNumberMultiply("1+-1i", "1+1i"))
print(Solution().complexNumberMultiply("1+1i", "1+1i"))
print(Solution().complexNumberMultiply("1+-1i", "1+-1i"))