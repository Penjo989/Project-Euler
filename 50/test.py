

def howMuch(n):
    b = n % 7
    sum = 0
    for k in range(n + 1):
        if k % 7 <= b:
            sum += 1
    return sum

def calcFunc(n):
    b = n % 7
    sum = b + 1
    for i in range(b + 1):
        sum += (n - i) // 7
    return sum

def main():
    for n in range(1000000):
        if howMuch(n) != calcFunc(n):
            print("ERROR")

main()