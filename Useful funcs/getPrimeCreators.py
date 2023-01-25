
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



def getDict():
    max = 12000
    dict = {1 : []}
    gen = primeGen()
    nextPrime = next(gen)
    while nextPrime <= max:
        keys = list(dict.keys())
        for key in keys:
            n = 1
            while key * (nextPrime ** n) <= max:
                dict[key * nextPrime ** n] = dict[key] + [nextPrime] * n
                n += 1
        nextPrime = next(gen)
    print(dict)
getDict()