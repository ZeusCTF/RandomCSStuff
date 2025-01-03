def checkTwoChessboards(coordinate1, coordinate2):
    if int(ord(coordinate1[0])) % 2 != 0 and int(coordinate1[1]) % 2 != 0:
        coordinate1 = 'black'
    else:
        coordinate1 = 'white'

    if int(ord(coordinate2[0])) % 2 != 0 and int(coordinate2[1]) % 2 != 0:
        coordinate2 = 'black'
    else:
        coordinate2 = 'white'

    if coordinate2 == coordinate1:
        print('same')
        return True
    else:
        print('not')
        return False

checkTwoChessboards('a1','c3')
        