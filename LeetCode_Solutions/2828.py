#first time trying a lambda function
def main(words, s):
    first = lambda words, s: ''.join(word[0] for word in words) == s
    result = first(words, s)
    print(result)
            
main(["alice","bob","charlie"], "abc")

