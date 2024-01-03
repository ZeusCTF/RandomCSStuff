
def recur(x, y):
    if x > 1:
        return recur(x - 1, y * (x - 1))
    else:
        return y

def main(x):
    i = 1
    i = recur((x+1), i)
    print(i)

main(5)