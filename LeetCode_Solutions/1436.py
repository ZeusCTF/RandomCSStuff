def main(paths):
    map = dict()
    for i in paths:
        map[i[0]] = i[1]
    print(map)
    for j in paths:
        if j[1] not in map:
            return j[1]

        



main([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])