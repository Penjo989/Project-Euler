

def main():
    maxVal = 0
    maxD = 2

    for d in range(2, 1001):
        if (d ** 0.5).is_integer():
            continue
        x = 2
        while True:
            y = (((x ** 2 - 1) / d) ** 0.5)
            print(d)
            if y.is_integer():
                print(f"x: {x} , y: {y}")
                if x > maxVal:
                    maxVal = x
                    maxD = d
                break
            x += 1
    print(maxD)



main()