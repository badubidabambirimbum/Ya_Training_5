min_x = 10**9 + 1
max_x = -1
min_y = 10**9 + 1
max_y = -1

with open("input.txt", "r") as input:
    k = int(input.readline())

    for i in range(k):
        x,y = list(map(int, input.readline().split()))
        max_x = max(x,max_x)
        min_x = min(x,min_x)
        max_y = max(y,max_y)
        min_y = min(y,min_y)

print(min_x,min_y,max_x,max_y)