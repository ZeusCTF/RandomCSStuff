def main(s):
    res = []

    for c in s:
        if c == '0' or c >= '9' and res:
            res.pop()
        else:
            res.append(c)
    print(res)

main("cb34")