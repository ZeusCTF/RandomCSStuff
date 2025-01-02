def uncommonFromSentences(s1, s2):
    string1 = s1.split(' ')
    string2 = s2.split(' ')
    ans = []

    collect1 = {}
    for word in string1:
        collect1[word] = 1 + collect1.get(word, 0)

    collect2 = {}
    for word in string2:
        collect2[word] = 1 + collect2.get(word, 0)

    combined = {key: collect1.get(key, 0) + collect2.get(key, 0) for key in collect1.keys() | collect2.keys()}

    for word in combined:
        if combined[word] == 1:
            ans.append(word)

    print(ans)
    return ans

uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour")
        