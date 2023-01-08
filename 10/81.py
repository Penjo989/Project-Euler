

def getPathSum(list):

    for i in range(1, len(list)):
        list[0][i] += list[0][i - 1]
        list[i][0] += list[i - 1][0]
        for j in range(1, i):
            list[j][i] += min(list[j][i - 1], list[j - 1][i])
            list[i][j] += min(list[i - 1][j], list[i][j - 1])
        list[i][i] += min(list[i - 1][i], list[i][i - 1])
    return list

def main():
    f = open('p081_matrix.txt', 'r')
    data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i].split(",")
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])

    l = getPathSum(data)
    print(l[79][79])





if __name__ == "__main__":
    main()