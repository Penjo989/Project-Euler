

def isPermutation(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    dict = {}
    if len(num1) != len(num2):
        return False
    for digit in num1:
        if digit not in dict.keys():
            dict[digit] = 1
        else:
            dict[digit] += 1
    for digit in num2:
        if digit not in dict.keys():
            return False
        else:
            dict[digit] -= 1
    for c in dict.values():
        if c != 0:
            return False
    return True


def calcPhi(p1, p2):
    return p1 * p2 - p1 - p2 + 1

f = open('primes.txt', 'r')
lines = f.readlines()
primes = []

for line in lines:
    line = line.strip().split("\t")
    primes += line
for i in range(len(primes)):
    primes[i] = int(primes[i])
primes.reverse()
minimum = - 1
minNum = 0
for i in range(len(primes) - 1):
    for j in range(i, len(primes) - 1):
        if isPermutation(calcPhi(primes[i], primes[j]), primes[i] * primes[j]):
            if minimum == -1 or primes[i] * primes[j] / calcPhi(primes[i] , primes[j]) < minimum:
                if(primes[i] * primes[j] < 10000000):
                    minimum = primes[i] * primes[j] / calcPhi(primes[i], primes[j])
                    minNum = primes[i] * primes[j]
                    print(f"num: {primes[i] * primes[j]}, phi: {calcPhi(primes[i], primes[j])} , {primes[i] * primes[j] / calcPhi(primes[i] , primes[j])}")
print(f"{minNum}\t {minimum}")