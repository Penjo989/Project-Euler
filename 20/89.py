
def romanToNumber(roman):
    sum = 0
    for letter in roman:
        if letter == 'I': sum += 1
        elif letter == 'V': sum += 5
        elif letter == 'X': sum += 10
        elif letter == 'L': sum += 50
        elif letter == 'C': sum += 100
        elif letter == 'D': sum += 500
        elif letter == 'M': sum += 1000
    return sum

def getMinLength(num, numOfChars = 0, maxC = 0, maxX = 0):
    minimum = 500
    numOfChars += num // 1000
    maxM = num // 1000
    num -= maxM * 1000
    if num >= 500:
        numOfChars += 1
        num -= 500
    maxC = max(num // 100, maxM - 1)
    num -= maxC * 100
    if num >= 50:
        numOfChars += 1
        num -= 50
    maxX = max(num // 10, maxC - 1)
    num -= maxX * 10

    numOfChars += num // 5 + num % 5

    return originalLen - numOfChars


def main():
    sum = 0
    f = open("romanNumbers.txt", 'r')
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    for roman in lines:
        sum += getCharsSaved(roman)
    print(sum)

main()