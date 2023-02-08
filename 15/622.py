
def main():
    sum = 0
    for i in range(0, 1000, 2):
        if (2 ** 8) % (i + 1) == 1:
            print(i)
    print(sum)
main()
