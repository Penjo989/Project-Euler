



for i in range(1, 1000):
    for j in range(i, 1000):
        print(i, j)
        if ((i ** 2 + j ** 2) ** 0.5).is_integer():
            if ((i ** 2 + j ** 2) ** 0.5) + i + j == 1000:
                print(i * j * ((i ** 2 + j ** 2) ** 0.5))
                exit()
