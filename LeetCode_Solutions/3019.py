def countKeyChanges(s):
    s = s.lower()
    count = 0
    first = s[0]

    for char in s:
        if first != char:
            count += 1
            first = char

    print(count)

countKeyChanges("aAbBcC")