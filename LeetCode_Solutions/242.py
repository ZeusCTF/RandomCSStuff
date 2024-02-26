def main(s, t):
    ans = False
    s_val = 0
    t_val = 0

    for letter in s:
        #s_val += s[letter]
        print(ord(s[letter]))
    
    for letter in t:
        t_val += t[letter]
    
    if s_val == t_val:
        ans = True
    
    return ans
    

main("anagram", "nagaram")