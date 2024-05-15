import base64

def encode(longurl):
    """Encodes a URL to a shortened URL.
    """
    enc = base64.b16encode(longurl.encode())
    base = "https://leetcode/" + enc.decode()
   # print(base)
    decode(base, enc)

def decode(url, enc):
    """Decodes a shortened URL to its original URL.
    """
    print(enc)
    print(url)
    s = ""
    for i in url[::-1]:
        if i == '/':
            s = s[::-1]
            
            print(base64.b16decode(s).decode())
            return base64.b16decode(s).decode()
        s += i
        
encode("http://badge.example.net/beginner.aspx?aftermath=achiever&actor=air")