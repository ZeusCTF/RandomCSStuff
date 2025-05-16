def truncateSentence(s, k):
    return ' '.join(s.split()[:k])

truncateSentence("Hello how are you Contestant", 4)