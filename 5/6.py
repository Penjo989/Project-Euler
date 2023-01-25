


sumOfSquares = 0
sqaureOfSums = 0

for i in range(101):
    sumOfSquares += i ** 2
    sqaureOfSums += i
sqaureOfSums **= 2

print(sumOfSquares - sqaureOfSums)