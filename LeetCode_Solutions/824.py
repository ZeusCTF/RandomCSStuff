def toGoatLatin(sentence):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    words = sentence.split()
    a_count = 1
    word_count = 0


    for word in words:
        if word[0] in vowels:
            words[word_count] += 'ma'
            words[word_count] += 'a' * a_count
        else:
            words[word_count] += word[0].lower()
            words[word_count] += 'ma'
            words[word_count] += 'a' * a_count
            words[word_count] = words[word_count][1:]
        word_count += 1
        a_count += 1
            

    print(words)
    return ' '.join(words)





toGoatLatin('I speak Goat Latin')

        
        










"""

    If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
        For example, the word "apple" becomes "applema".
    If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
        For example, the word "goat" becomes "oatgma".
    Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
        For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.
"""