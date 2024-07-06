def main(n, time):
    if time < n:
        return n - time
    else:
        return n - (time % n)

print(main(4, 5))