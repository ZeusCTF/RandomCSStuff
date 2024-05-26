def main(s):
    t = ''
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'y', 'Y']
    strVowel = []
    count = 0

    for letter in s:
        if letter in vowels:
            strVowel.append(ord(letter))

    if strVowel:
        strVowel.sort()
        for letter in s:
            if letter in vowels:
                t += chr(strVowel[count])
                count += 1
            else:
                t += letter
    print(t)

main("tst")