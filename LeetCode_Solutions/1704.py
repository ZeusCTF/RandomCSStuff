def main(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    half = round(len(s) / 2)
    lower = 0
    upper = len(s)
    ucount = 0
    lcount = 0
    ans = False

    for i in range(lower,half):
        print(s[i])
        if s[i] in vowels:
            lcount += 1

    for i in range(half,upper):
        if s[i] in vowels:
            ucount += 1

    print(lcount)
    print(ucount)
    if lcount == ucount:
        ans = True

    return False

main('book')