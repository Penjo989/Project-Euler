

def calcSum(l, h):
    return int((l ** 2 + l) * (h ** 2 + h) / 4)


def main():
    print(calcSum(3, 2))
    closest = 0
    closestSize = [0, 0]
    for l in range(1000):
        for h in range(l + 1, 1000):
            sum = calcSum(l, h)
            if abs(2000000 - sum) < abs(2000000 - closest) or closest == 0:
                closest = sum
                closestSize = [l, h]
    print(closest, closestSize)


main()