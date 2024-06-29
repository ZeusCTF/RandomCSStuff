def main(words, x):
    return [ i for i in range(len(words)) if x in words[i]]

main(["leet","code"], 'e')