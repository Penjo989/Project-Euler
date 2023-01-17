

def main():
    f = open("13 numbers.txt", "r")
    lines = f.readlines()
    numbers = []
    for line in lines:
        numbers.append(int(line.strip()))

    sum = 0
    for number in numbers:
        sum += number
    print(str(sum)[:10])
main()