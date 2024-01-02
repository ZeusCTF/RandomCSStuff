def main(word1, word2):
    
  w1 = ''.join(word1)
  w2 = ''.join(word2)

  if w1 == w2:
    print('yes')
  else:
    print('no')

main(['ab', 'c'],['a','bc'])