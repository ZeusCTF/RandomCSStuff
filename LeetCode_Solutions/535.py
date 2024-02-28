import base64
class Codec:

    def encode(self, longUrl):
        longUrl = base64.b64encode(longUrl.encode()).decode()
        print(longUrl.rstrip("="))


    def decode(self, shortUrl):
        pass
        

codec = Codec()
codec.encode("https://leetcode.com/problems/design-tinyurl")
# codec.decode(codec.encode(url))