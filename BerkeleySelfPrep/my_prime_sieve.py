def sieve(limit):
    l = []

    #creates dict and sets all initial values to prime
    is_prime = {i: 'prime' for i in range(2, limit + 1)}

    #sets the loop range to continue until it reaches the sqrt of the given limit
    for i in range(2, int(limit ** .5)+ 1):
        if is_prime[i] == 'prime':
            #steps through multiples of our new range
            for multiple in range(i*i, limit + 1, i):
                is_prime[multiple] = 'composite'

    for x in is_prime:
        if is_prime[x] == 'prime':
            l.append(x)

    print(is_prime)
    print(l)
    
sieve(20)