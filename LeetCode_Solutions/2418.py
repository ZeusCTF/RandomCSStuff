def main(names, heights):
    j = {}
    i = 0
    res = []

    while i < len(heights):
        j[heights[i]] = names[i]
        i += 1
    while j:
        x = max(j)
        res.append(j[x])
        del j[x]
    return res

main(["Mary","John","Emma"], [180,165,170])