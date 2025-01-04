def checkTwoChessboards(coordinate1, coordinate2):
    def cord_check(coord):
        first = int(ord(coord[0]))
        second = int(coord[1])

        if first % 2 != 0 and second % 2 != 0:
            coord = 'black'
            return coord
        elif first % 2 == 0 and second % 2 == 0:
            coord = 'black'
            return coord
        else:
            coord = 'white'
            return coord

    coordinate1 = cord_check(coordinate1)
    coordinate2 = cord_check(coordinate2)

    if coordinate2 == coordinate1:
        return True
    else:
        return False

checkTwoChessboards('a7','a6')