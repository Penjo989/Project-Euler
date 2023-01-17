import math
import time

#the code is too long for me to want to write it
#but my answer idea and part of it's execution is right
#bisect.insort(a, 3)
def isBigger(num1, num2):
    return math.log(num1[0], num2[0]) * num1[1] > num2[1]
def primeGen():
    primes = [2, 3, 5]
    for p in primes:
        yield p
    num = 7
    while True:
        for prime in primes:
            if prime > num ** 0.5 + 1:
                primes.append(num)
                yield num
                break
            if num % prime == 0:
                break
        num += 2

def increasePower(pow):
    return 2 * pow + 1

def main():
    primes = primeGen()
    dict = {2 : 0}
    lastPrime = next(primes)

    update = 0
    additionList = [2]
    for i in range(5):
        print(f"i: {i}\tdict: {dict}\tlist: {additionList}")
        update = additionList[0]
        if additionList[0] == lastPrime:
            dict[additionList[0]] = 1
            additionList = additionList[1:]
            lastPrime = next(primes)
            dict[lastPrime] = 0
            if len(additionList) == 0 or isBigger([lastPrime, 1], [additionList[-1], dict[additionList[-1]]]):
                additionList.append(lastPrime)
            else:
                for i in range(len(additionList)):
                    if isBigger([additionList[i], dict[additionList[i]]], [lastPrime, 1]):
                        additionList = additionList[:i + 1] + [lastPrime] + additionList[i + 1:]
                        break


        else:
            dict[additionList[0]] = increasePower(dict[additionList[0]])
            additionList = additionList[1:]

        additionList.append(update)


    print(dict)
    num = 1
    for key in dict.keys():
        num = (num * (key ** dict[key]) % 500500507) % 500500507
    print(num)
main()