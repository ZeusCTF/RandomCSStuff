def main(arr1, arr2):
    res = []

    d = {}
    for item in arr2:
        d[item] = arr2.index(item)

    for item in arr1:
        if item in d:
            res.insert(d[item], item)
        else:
            res.append(item)
    print(res)


main([28,6,22,8,44,17], [22,28,8,6])
