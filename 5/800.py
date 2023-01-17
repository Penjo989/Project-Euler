import math



def main():
    f = open('C:/Users\eyala\Desktop\Project euler\Project-Euler\\20\\primes.txt', 'r')
    lines = f.readlines()
    primes = []

    for line in lines:
        line = line.strip()
        primes += line
    print(lines[0].replace(" ", ""))
    return
    for i in range(len(primes)):
        try:
            primes[i] = int(primes[i])
        except:
            print(primes[i], "asdasd")
    primes = primes[:-2]
    #print(primes[-1])
    sum = 0
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            p = primes[i]
            q = primes[j]
            if math.log(p, 800800) * (q + math.log(q, p) * p) <= 800800:
                sum += 1
    print(sum)
main()