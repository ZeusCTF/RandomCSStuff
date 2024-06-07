def main(words):
    import collections

    ans=collections.Counter(words[0])
    for word in words:
        ans &=collections.Counter(word)
    return list(ans.elements()) 

main(["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"])