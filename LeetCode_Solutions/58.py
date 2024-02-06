def main(s):
    ans = 0

    i = len(s) - 1
    for letter in s[-1]:
        while letter == " ":
            print('space')
        while letter != " ":
            ans += 1
        print(ans)
        return
    
main('luffy is still joyboy    ')

"""
Thanks to built-in string methods, something like this works in Python and is much easier.  But...  I think an interviewer would prefer you to not use any built-in methods

ans = 0
    for letter in s.strip()[::-1]:
        if letter != ' ':
            ans += 1
        else:
            break
"""
