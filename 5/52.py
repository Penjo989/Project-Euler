


def check(i):
    i2 = str(2 * i)
    i3 = str(3 * i)
    i4 = str(4 * i)
    i5 = str(5 * i)
    i6 = str(6 * i)
    i = str(i)
    list = [i2, i3, i4, i5, i6]
    for mult in list:
        if len(mult) > len(i):
            return
        for digit in i:
            if digit not in mult:
                return
    print(i)


for i in range(1, 1000000):
    check(i)