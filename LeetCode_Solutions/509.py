def main(n):
    i = 0
    j = 1
    tot = 0

    if n == 0 or n == 1:
        return n

    for val in range(0, n-1):
        tot = i + j
        i = j
        j = tot
    return tot