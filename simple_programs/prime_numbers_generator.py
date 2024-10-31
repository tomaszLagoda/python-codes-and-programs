def genPrimes():
    primes = []
    num = 2

    while True:
        is_prime = True

        if num > 2:
            for x in primes:
                if (num % x) == 0:
                    is_prime = False
                    break
        
        if is_prime:
            primes.append(num)
            yield num
        
        num += 1

primeGenerator = genPrimes()
print(next(primeGenerator))
print(next(primeGenerator))
print(next(primeGenerator))
print(next(primeGenerator))
print(next(primeGenerator))

