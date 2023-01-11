
def getNextPrime(num):
    num += 1
    while True:
        for i in range(2,num):
            if num % i == 0:
                break
            if i == num - 1:
                return num

        num += 1
a = 2
maximum = 1
num = 600851475143
while a <= num:
    if num % a == 0:
        print(a)
        num /= a
        maximum = a
    a = getNextPrime(a)

print(maximum)