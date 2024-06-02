def main(x):
    x = str(x)
    if '-' in x:
        x = x.replace('-','')
        if 0 - (int(str(x)[::-1])) > -2147483648:
            return 0 - (int(str(x)[::-1]))
        else:
            return 0
    else:
        if int(str(x)[::-1]) < 2147483647:
            return int(str(x)[::-1])
        else:
            return 0
        
main(-123)