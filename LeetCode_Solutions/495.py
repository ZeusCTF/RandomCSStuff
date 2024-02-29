def main(timeSeries, duration):
    l = len(timeSeries)
    total = 0

    for occurance in range(l):
        if timeSeries[occurance + 1]:
            if timeSeries[occurance] + duration < timeSeries[occurance + 1]:
                total += duration

    print(total)
main([1,4],2)