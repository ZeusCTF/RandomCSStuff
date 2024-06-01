def main(costs, coins):
    bars = 0
    costs.sort()
    for price in costs:
        if price <= coins:
            coins -= price
            bars += 1
    return bars

main([1,3,2,4,1], 7)