


def main():
    sum = 0
    for i in range(2, 1000000):
        product = 0
        tempI = i
        while tempI > 0:
            product += (tempI % 10) ** 5
            tempI //= 10
        if product == i:
            sum += product
            print(product)
    print(sum)





if __name__ == "__main__":
    main()