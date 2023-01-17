from fractions import Fraction

def calc(a, b, c):
    return b + a * c, c


def main():
    numbers = [(2 * ((i - 1) // 3 + 1) if i == 1 or (i - 1) % 3 == 0 else 1) for i in range(99)]
    numbers[1] = 2
    numbers.reverse()
    nume = 1
    deno = numbers[0]
    for num in numbers[1:]:
        deno, nume = calc(num, nume, deno)

    nume, deno = calc(2, nume, deno)
    nume = str(nume)
    sum = 0
    for digit in nume:
        sum += int(digit)
    print(sum)
main()