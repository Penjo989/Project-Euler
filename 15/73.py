

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
    return dict

def dontHaveCommons(num1, num2, dict):
    for p in dict[num1]:
        if p in dict[num2]:
            return False
    return True
def main():
    sum = 0
    gen = primeGen()
    d = getDict()
    for i in range(3, 12001):
        for j in range(round((1 / 4) * i), int((1 / 2) * i + 1)):
            if 1 / 3 < j / i < 0.5 and dontHaveCommons(i, j, d):
                #print(f"{j} / {i}")
                sum += 1
    print(sum)

main()

