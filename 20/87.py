
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
    primes = [next(gen) for i in range(1000)]
    squares = []
    qubes = []
    fourthPows = []
    goodNumbers = set()
    for p in primes:
        if p ** 2 < 5 * 10 ** 7:
            squares.append(p ** 2)
        if p ** 3 < 5 * 10 ** 7:
            qubes.append(p ** 3)
        if p ** 4 < 5 * 10 ** 7:
            fourthPows.append(p ** 4)
    for s in squares:
        for q in qubes:
            for f in fourthPows:
                if s + q + f < 5 * 10 ** 7:
                    goodNumbers.add(s + q + f)

    print(len(goodNumbers))

main()