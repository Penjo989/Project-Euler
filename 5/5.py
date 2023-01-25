


def main():
    primes = [2, 3, 5 ,7, 11, 13, 17, 19]
    num = 1
    for p in primes:
        i = 0
        while p ** i <= 20:
            i += 1
        num *= p ** (i - 1)
    print(num)


main()