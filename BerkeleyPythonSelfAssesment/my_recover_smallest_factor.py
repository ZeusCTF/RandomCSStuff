def main(comp):
    i = 2
    while i * i <= comp:
        if comp % i == 0:
            print(f'Smallest prime factor: {i}')
            break
        else:
            i += 1
main(25)
