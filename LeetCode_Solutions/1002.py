def main(words):
    d = {}

    for char in range(ord('a'), ord('z') + 1):
        char = chr(char)
        for word in words:
            if char in word:
                d[char] = d.get(char, 0) + word.count(char)
    print(d)

main(["bella","label","roller"])