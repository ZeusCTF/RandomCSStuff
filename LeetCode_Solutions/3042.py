def countPrefixSuffixPairs(words):
    res = 0
    n = len(words)

    for i in range(0, n):
        for j in range(i + 1, n):

            if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                res += 1
    print(res)

countPrefixSuffixPairs(["bb","bb"])