def main(a,b):
    res = ""
    carry = 0

    for i in range(max(len(a), len(b))):
        digitA = a[i] if i < len(a) else 0
        digitB = b[i] if i < len(b) else 0

        print(digitA, digitB)

main("11", "1")