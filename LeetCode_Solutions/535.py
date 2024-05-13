import base64

def encode(longurl):
    """Encodes a URL to a shortened URL.
    """
    enc = base64.b64encode(longurl.encode())
    base = "https://leetcode/" + enc.decode()
    print(base)
    decode(base)

def decode(url):
    """Decodes a shortened URL to its original URL.
    """
    s = ""
    for i in url[::-1]:
        if i == '/':
            s = s[::-1]
            
            return base64.b64decode(s).decode()
        s += i
encode("https://leetcode.com/problems/design-tinyurl")