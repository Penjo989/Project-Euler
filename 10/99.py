import math
def isBigger(num1, num2):
    return math.log(num1[0], num2[0]) * num1[1] > num2[1]

def main():
    f = open("99 file.txt", 'r')
    lines = f.readlines()
    for j in range(len(lines)):
        lines[j] = lines[j].split(",")
        for i in range(len(lines[j])):
            lines[j][i] = int(lines[j][i])
    maxVal = lines[0]
    maxLine = 0
    for j in range(len(lines)):
        if isBigger(lines[j], maxVal):
            maxVal = lines[j]
            maxLine = j
    print(maxLine + 1)


if __name__ == "__main__":
    main()