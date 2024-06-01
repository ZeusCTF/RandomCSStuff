def main(s):
    x = 0
    y = 1
    res = 0

    while y < len(s):
        val = abs((ord(s[x])) - ord(s[y]))
        x += 1
        y += 1
        res += val

    print(res)

main('hello')