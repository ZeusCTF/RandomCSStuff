def main(n):
    i = 1
    x = 0
    while n:
        y = i + x
        x = i
        i = y
        n -= 1
    return y

main(4)