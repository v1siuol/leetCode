"""
Success
Details 
Runtime: 28 ms, faster than 96.06% of Python online submissions for Bulls and Cows.
Memory Usage: 11.9 MB, less than 7.94% of Python online submissions for Bulls and Cows.
"""

# diss 有更简单的 

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        dct_secret = dict()
        for loc, val in enumerate(secret):
            if val not in dct_secret:
                dct_secret[val] = dict()
                dct_secret[val]['avail_count'] = 1
                dct_secret[val]['loc'] = set((loc,))
            else:
                dct_secret[val]['loc'].add(loc)
                dct_secret[val]['avail_count'] += 1

        # print(dct_secret)

        bulls = 0
        cows = 0
        for loc, val in enumerate(guess):
            if val in dct_secret:
                if loc in dct_secret[val]['loc']:
                    bulls += 1
                    dct_secret[val]['avail_count'] -= 1

        for loc, val in enumerate(guess):
            if val != secret[loc]:
                if val in dct_secret and dct_secret[val]['avail_count'] > 0:
                        cows += 1
                        dct_secret[val]['avail_count'] -= 1


        return '{}A{}B'.format(bulls, cows)



s = Solution()


print(s.getHint("1807", "7810") == '1A3B')
print(s.getHint("1107", "7110") == '1A3B')

print(s.getHint("1123", "0111") == '1A1B')

print(s.getHint("1122", "1222") == "3A0B")


