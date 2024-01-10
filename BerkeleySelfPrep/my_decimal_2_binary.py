def main(num):
    ans = ''
    print('Decimal form', str(num))
    while num > 0:
        ans += str(num % 2)
        num //= 2
    print('Binary form:', ans)
main(5)

