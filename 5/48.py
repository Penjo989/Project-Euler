



def main():
    sum = 0
    for i in range(1, 1000):
        num = 1
        for j in range(i):
            num = (num * i) %( 10 ** 10)
        sum += num
    print(sum % (10 ** 10))




if __name__ == "__main__":
    main()