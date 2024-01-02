def main(words, chars):
    test = {}
    value = 0

    for char in chars:
        #creates a frequency hashmap, if a character is encountered more than once it is incremented
        test[char] = 1 + test.get(char, 0)
    for word in words:
        tset = test.copy()
        for letter in word:
            if letter in tset and tset[letter] != 0:
                tset[letter] -= 1
            else:
                tset = test.copy()
                break
        value += sum(test.values()) - sum(tset.values())
    print(value)
main(["hello","world","leetcode"], "welldonehoneyr")