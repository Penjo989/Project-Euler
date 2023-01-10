import time
"""
#this code works but takes a long time to calculate
#the actual solution is purely mathematical.
dict = {1: []}
def main():
    maximum = 0
    maxNum = 1
    limit = 1000000
    for n in range(2, limit + 1):
        print(n)
        if n not in dict.keys():
            newDict = {}
            for num in dict.keys():
                i = 1
                res = num * (n ** i)
                while res <= limit:
                    newDict[res] = list(dict[num])
                    newDict[res].append(n)
                    i += 1
                    res = num * (n ** i)
            keys = list(newDict.keys())
            for j in range(len(keys)):
                dict[keys[j]] = newDict[keys[j]]
        if n / (n - getNumOfCommons(dict[n], n) - 1) > maximum:
            maxNum = n
            maximum = n / (n - getNumOfCommons(dict[n], n) - 1)
            #print(f"n: {n}\t{maximum}")
    print(f"maxNum: {maxNum}\tvalue: {maximum}")

def getNumOfCommons(list, n):
    sum = 0
    for i in range(len(list)):
        sum += int(n / list[i]) - 1
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            sum -= int(n / (list[i] * list[j])) - 1
    return sum

"""
def main():
    n = 1
    k = 0
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 29, 31]
    while primes[k] * n <= 1000000:
        n *= primes[k]
        k += 1
    print(n)



if __name__ == "__main__":
    main()