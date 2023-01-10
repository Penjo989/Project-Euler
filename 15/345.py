

def getMatSum(matrix, row, usedColumns):
    maxSum = 0
    for i in range(len(matrix[0])):
        if i not in usedColumns:
            if row == len(matrix) - 1:
                return matrix[row][i]
            maxSum = max(maxSum, getMatSum(matrix, row + 1, usedColumns + [i]) + matrix[row][i])
    return maxSum

def main():
    f = open("345 matrix.txt", 'r')
    lines = f.readlines()
    for j in range(len(lines)):
        lines[j] = lines[j].split(" ")
        for i in range(len(lines[j])):
            lines[j][i] = int(lines[j][i])

    test = [[7 , 53, 183 ,439, 863],
        [497 ,383 ,563 , 79 ,973],
        [287 , 63 ,343 ,169 ,583],
        [627, 343, 773 ,959, 943],
        [767 ,473, 103 ,699 ,303]]
    matSum = getMatSum(lines, 0, [])
    print(matSum)


if __name__ == "__main__":
    main()