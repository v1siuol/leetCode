"""
100 / 100 test cases passed.
Status: Accepted
Runtime: 46 ms
You are here!
Your runtime beats 43.94% of python submissions.
"""
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        def c2c(bNum):
            #bNum = input("Number: ")
            def toggle(st):
                return "1" if st == "0" else "0"
            #while "".zfill(len(bNum)) != bNum and "".zfill(len(bNum)) == bNum.replace("1", "0"):
            result = list(map(toggle, bNum))  # 1's complement
            n = -1  # end position
            while True:
                # animation of 1 + 1's complement
                if result[n] == "0":
                    result[n] = toggle(result[n])
                    break
                else:
                    result[n] = toggle(result[n])
                    n -= 1
            return "".join(result)

        def cnm(s):
            re = ""
            i = 0
            dic = {"0000": "0", "0001":"1", "0010":"2", "0011":"3", "0100":"4", "0101":"5", "0110":"6",
                   "0111":"7", "1000":"8", "1001":"9", "1010":"a", "1011":"b", "1100":"c", "1101":"d",
                   "1110": "e", "1111":"f"}
            while i < len(s):
                re += dic[s[i:i+4]]
                i += 4

            while re[0] == "0":
                #re = re[j:0]
                #print(j, re)

                re = re[1:]
            return re
        tnum = bin(num)

        if num < 0:
            #print(tnum)
            r = c2c(tnum[3:])
            f = "1" * (32-len(r)) + r
        elif num == 0:
            return "0"
        else:
            r = tnum[2:]
            f = "0" * (32-len(r)) + r
        return cnm(f)


print(Solution().toHex(26))
print(Solution().toHex(-1))
print(Solution().toHex(12))