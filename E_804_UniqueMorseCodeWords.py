"""
Author  => v1siuol
Date    => 2018.05.07
83 / 83 test cases passed.
Status: Accepted
Runtime: 40 ms
You are here! 
Your runtime beats 93.72 % of python3 submissions.
"""
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # dct = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = set()
        dct = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-",'l':".-..", 'm':"--", 'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}

        for word in words:
            sig = ''
            for j in word:
                sig += dct[j]
            res.add(sig)

        # print(len(dct))
        return len(res)

print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
