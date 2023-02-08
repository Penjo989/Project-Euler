def primeGen():
    primes = [2, 3, 5]
    for p in primes:
        yield p
    num = 7
    while True:
        for prime in primes:
            if prime > num ** 0.5 + 1:
                primes.append(num)
                yield num
                break
            if num % prime == 0:
                break
        num += 2




def main():
    gen = primeGen()
    nextPrime = next(gen)
    sum = 0
    while nextPrime < 2 * 10 ** 6:
        sum += nextPrime
        nextPrime = next(gen)
    print(sum)
main()