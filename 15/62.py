
def isPermutation(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    if len(num1) != len(num2):
        return False
    d1 = {}
    for i in range(len(num1)):
        if num1[i] not in d1.keys():
            d1[num1[i]] = 1
        else:
            d1[num1[i]] += 1
        if num2[i] not in d1.keys():
            d1[num2[i]] = -1
        else:
            d1[num2[i]] -= 1
    for key in d1.keys():
        if d1[key] != 0:
            return False
    return True


def main():
    dict1 = {}

    for num in range(5000, 20000):
        qube = num ** 3
        if num % 1000 == 0:
             print(num)
        keys = dict1.keys()
        status = False
        for key in keys:
            if isPermutation(key, qube):
                dict1[key].append(num)
                status = True
                break
        if not status:
            dict1[qube] = [num]
    keys = dict1.keys()
    list = []
    d = {}
    for key in keys:
        if len(dict1[key]) == 5:
            d[key] = dict1[key]
            list += dict1[key]
    min = list[0]
    for num in list:
        if num < min:
            min = num
    print(min)

main()
