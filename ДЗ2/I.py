nums = []
with open("input.txt", "r") as input:
    n = int(input.readline())
    matrix = [[-1] * n for i in range(n)]
    for i in range(n):
        x,y = list(map(int, input.readline().split()))
        nums.append([x-1,y-1])
        matrix[x-1][y-1] = 0

nums.sort()

columns = [0] * n
sm_col = [0] * n
for i in range(len(nums)):
    x,y = nums[i]
    for j in range(len(columns)):
        if y != j:
            while matrix[columns[j]][j] != -1:
                columns[j] += 1
            matrix[columns[j]][j] = abs(columns[j] - x) + abs(j - y)
            sm_col[j] += matrix[columns[j]][j]
            columns[j] += 1

print(min(sm_col))