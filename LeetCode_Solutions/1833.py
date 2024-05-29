def main(costs, coins):
    x = 0
    y = len(costs) - 1
    bars = 0
    runs = 0

    while coins and x < y:
        #print(coins)
        #print(f"pass: {runs}")
        if costs[x] <= coins:
            print(x)
            coins -= costs[x]
            bars += 1
            x += 1
        if costs[y] <= coins:
            print(y)
            coins -= costs[y]
            bars += 1
            y -= 1
        runs += 1
    print(bars)
    






main([1,3,2,4,1], 7)