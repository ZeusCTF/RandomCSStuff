def findComplement(num):
    binary = '{0:b}'.format(num)
    flippers = ''

    for num in binary:
        if num == '1':
            flippers += '0'
        else:
            flippers += '1'
    print(flippers)
    print(int(flippers, 2))


findComplement(5)
