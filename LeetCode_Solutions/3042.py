def countPrefixSuffixPairs(words):
    res = 0

    for i in words:
        for j in words:
            if i == j:
                continue
            if words.index(i) > words.index(j):
                quit
            elif j.startswith(i) and j.endswith(i):
                res += 1
    print(res)

countPrefixSuffixPairs(["b","b","bb"])