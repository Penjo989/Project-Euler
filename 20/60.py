

def isPrime(num):
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

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
    primes = [next(gen) for i in range(200)]
    dictP = {p: [] for p in primes}
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if isPrime(int(str(primes[i]) + str(primes[j]))) and isPrime(int(str(primes[j]) + str(primes[i]))):
                dictP[primes[i]].append(primes[j])
                dictP[primes[j]].append(primes[i])
    print(dictP)

main()
