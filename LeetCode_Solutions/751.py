def main(heights):
    res = 0
    count = 0

    copy = heights[:]
    copy.sort()

    if copy == heights:
        return 0
    
    for i in heights:
        if i == copy[count]:
            count += 1
            pass
        else:
            res += 1
            count += 1

    return res




main([1,1,4,2,1,3])