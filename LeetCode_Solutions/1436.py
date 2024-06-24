def main(paths):
    map = dict()
    for i in paths:
        map[i[0]] = i[1]
    print(map)

        



main([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])