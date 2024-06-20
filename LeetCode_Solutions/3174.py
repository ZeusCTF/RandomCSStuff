def main(s):
    res = []
    nums = ['1','2','3','4','5','6','7','8','9','0']

    for c in s:
        if c in nums:
            res.pop()
        else:
            res.append(c)
    print(''.join(res))

main("cab34")