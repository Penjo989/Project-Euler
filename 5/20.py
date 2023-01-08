

def factorial(num):
    if num == 0: return 1
    return num * factorial(num - 1)

def main():
    x = str(factorial(100))
    sum = 0
    for digit in x:
        sum += int(digit)
    print(sum)






if __name__ == "__main__":
    main()