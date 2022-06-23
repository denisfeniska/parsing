matrix = [[y*x for y in range(1, 11)] for x in range(1, 11)]

for i in range(len(matrix)):
    print(*matrix[i])
