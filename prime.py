def primes_upto(n):
    primes = []
    for i in range(2, n+1):
        if all(i % j != 0 for j in range(2, int(i**0.5)+1)):
            primes.append(i)
    return primes

print(primes_upto(20))
