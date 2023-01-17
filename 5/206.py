import math

def isSpecial(num):
    j = 1
    for i in range(0, len(num) - 1, 2):
        if num[i] != str(j):
            return False
        j += 1
    if num[-1] == "0":
        return True
    return False


def main():
    start = int(math.sqrt(10203040506070809)) - 8
    print(start)
    while 1:
        start += 4 if start % 10 == 3 else 6
        sqaure = str(start * start)
        print(sqaure)
        if isSpecial(sqaure * 100):
            print(sqaure)
            return
        #print(sqaure)
main()