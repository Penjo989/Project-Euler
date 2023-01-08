
#https://en.wikipedia.org/wiki/Nim#:~:text=In%20ordinary%20Nim%20one%20forms,is%20zero%20for%20every%20digit.
"""
bad solution
def main():
    sum = 0
    for n in range(1, 2 ** 30 + 1):
        if (n ^ (2 * n)) ^ (3 * n) == 0: sum += 1
    print(sum)
"""

def main():
    a = 0
    b = 1
    for i in range(32):
        a, b = b, a + b
    print(a)


if __name__ == "__main__":
    main()