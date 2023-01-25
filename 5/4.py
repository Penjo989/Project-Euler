

def isPoli(numStr):
    for i in range(len(numStr) // 2):
        if numStr[i] != numStr[-(i + 1)]:
            return False

    return True

def main():
    maxPoli = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            if isPoli(str(i * j)):
                maxPoli = max(i * j, maxPoli)
    print(maxPoli)

main()