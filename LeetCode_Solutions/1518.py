def main(numBottles, numExchange):
    i = numBottles // numExchange
    x = numBottles - (i * numExchange)
    y = i + x
    res = numBottles + i


    while y >= numExchange:

        i = y // numExchange
        x = y - (i * numExchange)
        y = i + x


        res += i

        
    return res
         


print(main(17,3))