def main(edges):
    if edges[0][0] == edges[1][0]:
        return edges[0][0]
    elif edges[0][0] == edges[1][1]:
        return edges[0][0]
    else:
        return edges[0][1]


main([[1,2],[5,1],[1,3],[1,4]])