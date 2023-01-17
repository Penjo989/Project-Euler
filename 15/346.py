
def calcNumber(i, numOfOnes):
    num = 0
    while numOfOnes > 0:
        num += i ** (numOfOnes - 1)
        numOfOnes -= 1
    return num

def getGoodNumbers(numOfOnes, max):
    i = 2
    num = calcNumber(i, numOfOnes)
    serOfNumbers = set()
    while num < max:
        serOfNumbers.add(num)
        i += 1
        num = calcNumber(i, numOfOnes)
    return serOfNumbers


def main():
    goodNumbers = [getGoodNumbers(i, 10 ** 12) for i in range(3, 40)]
    for i in range(1, len(goodNumbers)):
        goodNumbers[0].update(goodNumbers[i])
    sum = 0
    for goodNum in goodNumbers[0]:
        sum += goodNum
    print(sum + 1)
main()
