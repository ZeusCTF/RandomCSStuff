def main(words):
    for char in range(ord('a'), ord('z') + 1):
        for word in words:
            if char in word:
                print(word, char)
        
main(["bella","label","roller"])