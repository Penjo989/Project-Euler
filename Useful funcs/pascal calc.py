
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)

def howMuchSevens(n):
    sum = 0
    for k in range(n):
        if ((factorial(n)) / (factorial(k) * factorial(n - k))) % 7 == 0:
            sum += 1
    return sum

def calc(n):
    j = 1
    sum = 0
    while True:
        if n < (7 ** j):
            break
        b = n % (7 ** j)
        sum += n - b
        for i in range(b + 1):
            sum -= (n - i) // (7 ** j)
        j += 1
    return sum


def main():
    for n in range(0, 100):
        print(f"n: {n} \t Expected: {howMuchSevens(n)}\t Got: {calc(n)}")

main()