"""
Author  => v1siuol
Date    => 2018.06.01
739 / 739 test cases passed.
Status: Accepted
Runtime: 71 ms
You are here! 
Your runtime beats 13.20 % of python submissions.
"""
import random
class Codec:

    
    def __init__(self):
        self.stor = dict()

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        base = "http://tinyurl.com/"
        zidian = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
        if longUrl in self.stor.values():
            return self.stor.get(longUrl)
        else:
            tail = "".join([random.choice(zidian) for _ in range(6)])
            while tail in self.stor.keys():
                tail = "".join([random.choice(zidian) for _ in range(6)])
            self.stor[tail] = longUrl
                
        return base+tail

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        print(self.stor)
        return self.stor[shortUrl[19:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))