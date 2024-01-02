def main(binary):
    num = 0
    for i, bit in enumerate(reversed(binary)):
        if bit == '1':
            num += 2 ** i
            print(f'Power of 2: {i}')
            print(f'Power of 2 value: {2 ** i}')
    print(num)
main('1011')
