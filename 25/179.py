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
    for i in range(4999999):
        print(i)
        next(gen)
    print(next(gen))

main()