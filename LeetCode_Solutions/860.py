def main(bills):
    fives = 0
    tens = 0
    twentys = 0

    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            if fives:
                fives -= 1
            else:
                return False
            tens += 1
        else:
            if tens and fives:
                tens -= 1
                fives -= 1
            elif fives >= 3 and not tens:
                fives -= 3
            else:
                return False
            twentys += 1
    return True


print(main([5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]))