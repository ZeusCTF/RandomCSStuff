def main(s, t):
    ans = False
    s_chars = {}
    t_chars = {}

    for char in s:
        s_chars[char] = 1 + s_chars.get(char, 0)

    for char in t:
        t_chars[char] = 1 + t_chars.get(char, 0)
    
    if s_chars == t_chars:
        ans = True
    
    return ans
    

main("anagram", "nagaram")

