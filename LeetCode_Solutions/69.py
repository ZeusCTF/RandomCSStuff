def main(x):
    lower = 0
    upper = x

    while True:
        test = (upper + lower) // 2
        test_squared = test * test

        if test_squared == x:
            print(test)
            return test
        elif test_squared > x:
            upper = test
        elif test_squared < x:
            lower = test


main(100)

#this works, but not fast enough