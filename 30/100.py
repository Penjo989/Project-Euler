import math



def main():
    n = 1

    while True:
        bn = round(((1 + math.sqrt(2)) ** (2 * n - 1) - (1 - math.sqrt(2)) ** (2 * n - 1)) / (2 * math.sqrt(2)))

        an = (1 + math.sqrt(2 * (bn ** 2) - 1)) / 2

        m = (1 + math.sqrt(2 * (an ** 2) - 2 * an + 1)) / 2

        totalDisks = (1 + math.sqrt(8 * (m ** 2) - 8 * m + 1)) / 2

        if totalDisks >= 10 ** 12:
            print(int(m))
            break
        n += 1



main()