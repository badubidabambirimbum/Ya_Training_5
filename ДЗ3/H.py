from collections import defaultdict

A = list()
B = list()

with open("input.txt", "r") as input:
    n = int(input.readline())
    for i in range(n):
        x1,y1,x2,y2 = list(map(int, input.readline().split()))
        if x1 < x2:
            A.append([x1,y1,x2,y2])
        elif x1 == x2:
            if y1 < y2:
                A.append([x1,y1,x2,y2])
            else:
                A.append([x2,y2,x1,y1])
        else:
            A.append([x2,y2,x1,y1])
    for i in range(n):
        x1,y1,x2,y2 = list(map(int, input.readline().split()))
        if x1 < x2:
            B.append((x1,y1,x2,y2))
        elif x1 == x2:
            if y1 < y2:
                B.append((x1,y1,x2,y2))
            else:
                B.append((x2,y2,x1,y1))
        else:
            B.append((x2,y2,x1,y1))

res = len(A)
S = set(B)
dist = defaultdict(int)

i = 0
while i < len(A):
    j = 0
    while j < len(B):
        x_a = A[i][2] - A[i][0]
        y_a = A[i][3] - A[i][1]
        x_b = B[j][2] - B[j][0]
        y_b = B[j][3] - B[j][1]

        if x_a == x_b and y_a == y_b:
            delta_x = B[j][0] - A[i][0]
            delta_y = B[j][1] - A[i][1]
            dist[(delta_x,delta_y)] += 1

        j += 1
    i += 1

for key in dist:
    if len(A) - dist[key] < res:
        res = len(A) - dist[key]

print(res)