"""
Success
Details 
Runtime: 72 ms, faster than 88.13% of Python online submissions for Encode and Decode Strings.
Memory Usage: 12 MB, less than 94.52% of Python online submissions for Encode and Decode Strings.
"""
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        ret = ''
        for word in strs:
            ret += word.replace('#', '##') + ' # '
        return ret

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        lst = s.split(' # ')[:-1]
        return list(map(lambda x: x.replace('##', '#'), lst))


# Your Codec object will be instantiated and called as such:
codec = Codec()
# codec.decode(codec.encode(strs))
strs = ['1', '2']
# print(codec.encode(strs))
print(codec.decode(codec.encode(strs)))

