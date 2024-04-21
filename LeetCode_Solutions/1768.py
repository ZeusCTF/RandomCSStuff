def mergeAlternately(word1, word2):
    def build(max, min, maxWord):
        ans = ""
        for i in range(0,min):
            ans += word1[i]
            ans += word2[i]
        for i in range((min+1), max):
            ans += maxWord[i]
        return ans
    
    len1 = len(word1)
    len2 = len(word2)

    if len2 > len1:
        print(build(len2, len1, word2))
    elif len1 > len2:
        print(build(len1, len2, word1))

mergeAlternately('test', 'cqdvw')