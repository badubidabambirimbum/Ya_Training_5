matrix = [[0] * 10 for i in range(10)]
p = 0

with open("input.txt", "r") as input:
    n = int(input.readline())
    for i in range(n):
        x,y = list(map(int, input.readline().split()))
        matrix[x][y] = 1

for i in range(1,9):
    for j in range(1,9):
        if matrix[i][j] == 1:
            if matrix[i+1][j] == 0:
                p += 1
            if matrix[i][j+1] == 0:
                p += 1
            if matrix[i-1][j] == 0:
                p += 1
            if matrix[i][j-1] == 0:
                p += 1

print(p)