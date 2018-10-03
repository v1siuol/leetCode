"""
10 / 10 test cases passed.
Status: Accepted
Runtime: 43 ms
You are here!
Your runtime beats 86.10% of python submissions.
"""
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # 排列组合
        def plzh(lst, d, size=1):
            temp = lst[:]
            c = 0
            re = [""]
            while c < d:
                for j in re[:]:
                    try:
                        dot = temp.index(j[(c-1)*size:])
                    except (IndexError, ValueError):
                        dot = -1
                    temp = temp[dot + 1:]
                    for k in temp:
                        re.append(j + k)
                    re.remove(j)
                    temp = lst[:]
                c += 1
            return re if re[0] != "" else []

        re = []
        clk = ["h0", "h1", "h2", "h3", "m0", "m1", "m2", "m3", "m4", "m5"]
        toClk = {"h0": 8, "h1": 4, "h2": 2, "h3": 1, "m0": 32, "m1": 16, "m2": 8, "m3": 4, "m4": 2, "m5": 1}
        combine = plzh(clk, num, 2)  # 返回空在0
        if len(combine) == 0:
            return ["0:00"]
        for i in combine:
            c = 0
            h = 0
            m = 0
            while c < len(i):
                if i[c] == "h":
                    h += toClk[i[c:c+2]]
                else:
                    m += toClk[i[c:c+2]]
                c += 2
            if h <= 11 and m <= 59:
                adM = "0"+str(m) if m < 10 else str(m)
                re.append(str(h)+":"+adM)
        return re

print(Solution().readBinaryWatch(1))