"""
Author  => v1siuol
Date    => 2018.05.13
52 / 52 test cases passed.
Status: Accepted
Runtime: 64 ms
You are here! 
Your runtime beats 98.76 % of python3 submissions.
"""
class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        rd = dict()
        for sigd in cpdomains:
            icnt = int(sigd.split()[0])
            tdmn = sigd.split()[1]

            if tdmn in rd:
                rd[tdmn] += icnt
            else:
                rd[tdmn] = icnt

            while len(tdmn.split('.')) > 1:
                tdmn = '.'.join(tdmn.split('.')[1:])
                if tdmn in rd:
                    rd[tdmn] += icnt
                else:
                    rd[tdmn] = icnt

        rl = list()
        for key, value in rd.items():
            rl.append(str(value)+' '+key)
        return rl
        
print(Solution().subdomainVisits(["9001 discuss.leetcode.com"]))
