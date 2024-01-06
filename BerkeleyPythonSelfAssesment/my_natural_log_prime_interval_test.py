import math

def sieve(limit):
    l = []
    is_prime = {i: 'prime' for i in range(2, limit + 1)}
    for i in range(2, int(limit ** .5)+ 1):
        if is_prime[i] == 'prime':
            for multiple in range(i*i, limit + 1, i):
                is_prime[multiple] = 'composite'
    for x in is_prime:
        if is_prime[x] == 'prime':
            l.append(x)
    return l

def logPrime(primes):
    pass

print(math.log(11))