def prefixCount(words, pref):
    res = 0
    for word in words:
        if word.startswith(pref):
            res += 1
    print(res)

prefixCount(["pay","attention","practice","attend"], 'at')