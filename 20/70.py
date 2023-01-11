
f = open('primes.txt', 'r')
lines = f.readlines()
primes = []
for line in lines:
    line = line.strip().split("\t")
    primes += line

def isPermutation(prime):
    phi = str(int(prime) - 1)
    if len(phi) != len(prime):
        return
    for digit in phi:
        if digit not in prime:
            print(prime, phi)
            return

for prime in primes:
    if(isPermutation(prime)):
        print(prime)