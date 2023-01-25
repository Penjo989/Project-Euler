

def main():
    a = 1
    b = 1
    sum = 0
    while b <= 4 * 10 ** 6:
        tempB = b
        b += a
        a = tempB
        if b % 2 == 0:
            sum += b
    print(sum)


main()