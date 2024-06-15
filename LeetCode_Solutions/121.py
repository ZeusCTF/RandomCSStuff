def main(prices):
    low = min(prices)
    lindex = prices.index(low)
    count = prices.index(low) + 1
    most = 0

    while count != len(prices):
        if prices[count] - prices[lindex] > most:
            most = prices[count] - prices[lindex]
            count += 1
        else:
            count += 1

    print(most)

main([7,1,5,3,6,4])