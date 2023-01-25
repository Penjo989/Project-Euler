

def isPenta(P):
    return (((P * 24 + 1) ** 0.5 + 1) / 6).is_integer()


def main():
    pentas = [int(n * (3 * n - 1) / 2) for n in range(1,20000)]

    minD = -1
    for i in range(10000):
        for j in range(i, 10000):
            if isPenta(pentas[i] + pentas[j]):
                if isPenta(pentas[j] - pentas[i]):
                    if minD == -1:
                        minD = pentas[j] - pentas[i]
                    else:
                        minD = min(pentas[j] - pentas[i], minD)
    print(minD)


main()
