matrix = []

with open("input.txt", "r") as input:
    m, n = list(map(int, input.readline().split()))
    for i in range(m):
        matrix.append(input.readline().split()[0])

dataset = []
res = [[""] * n for i in range(m)]

for i in range(m):
    j = 0
    while j < n:
        data = [-1] * 3
        while j < n and matrix[i][j] != "#":
            res[i][j] = matrix[i][j]
            j += 1

        if j != n:
            data[0] = i
            data[1] = j
        while j < n and matrix[i][j] == "#":
            res[i][j] = matrix[i][j]
            j += 1
        if data[0] != -1:
            data[2] = j - 1
            dataset.append(data)

output = False

if len(dataset) == 0:
    output = False
elif len(dataset) == 1:
    if dataset[0][2] - dataset[0][1] + 1 >= 2:
        res[dataset[0][0]][dataset[0][1]] = "a"
        for i in range(dataset[0][1] + 1, dataset[0][2] + 1):
            res[dataset[0][0]][i] = "b"
        output = True
    else:
        output = False
elif len(dataset) == 2:
    for i in range(dataset[0][1], dataset[0][2] + 1):
        res[dataset[0][0]][i] = "a"
    for i in range(dataset[1][1], dataset[1][2] + 1):
        res[dataset[1][0]][i] = "b"
    output = True
else:
    count = 0
    i = 0
    target = 0
    while i < len(dataset):
        y = dataset[i][0] - 1
        for j in range(i, len(dataset)):
            if dataset[j][0] - y == 1 and dataset[j][1] == dataset[i][1] and dataset[j][2] == dataset[i][2]:
                target = j + 1
                if count == 0:
                    if j == len(dataset) - 1:
                        for u in range(dataset[i][1], dataset[i][2] + 1):
                            res[dataset[j][0]][u] = "b"
                    else:
                        for u in range(dataset[i][1], dataset[i][2] + 1):
                            res[dataset[j][0]][u] = "a"
                elif count == 1:
                    for u in range(dataset[i][1], dataset[i][2] + 1):
                        res[dataset[j][0]][u] = "b"
                y = dataset[j][0]
            else:
                target = j
                break
        count += 1
        i = target
    if count <= 2:
        output = True
    else:
        output = False

if output == True:
    print("YES")
    for k in res:
        print(''.join(k))

else:
    dataset_y = []
    res = [[""] * n for i in range(m)]

    for i in range(n):
        j = 0
        while j < m:
            data = [-1] * 3
            while j < m and matrix[j][i] != "#":
                res[j][i] = matrix[j][i]
                j += 1

            if j != m:
                data[0] = i
                data[1] = j
            while j < m and matrix[j][i] == "#":
                res[j][i] = matrix[j][i]
                j += 1
            if data[0] != -1:
                data[2] = j - 1
                dataset_y.append(data)

    if len(dataset_y) == 0:
        output = False
    elif len(dataset_y) == 1:
        if dataset_y[0][2] - dataset_y[0][1] + 1 >= 2:
            res[dataset_y[0][1]][dataset_y[0][0]] = "a"
            for i in range(dataset_y[0][1] + 1, dataset_y[0][2] + 1):
                res[i][dataset_y[0][0]] = "b"
            output = True
        else:
            output = False
    elif len(dataset_y) == 2:
        for i in range(dataset_y[0][1], dataset_y[0][2] + 1):
            res[i][dataset_y[0][0]] = "a"
        for i in range(dataset_y[1][1], dataset_y[1][2] + 1):
            res[i][dataset_y[1][0]] = "b"
        output = True
    else:
        count = 0
        i = 0
        target = 0
        while i < len(dataset_y):
            x = dataset_y[i][0] - 1
            for j in range(i, len(dataset_y)):
                if dataset_y[j][0] - x == 1 and dataset_y[j][1] == dataset_y[i][1] and dataset_y[j][2] == dataset_y[i][
                    2]:
                    target = j + 1
                    if count == 0:
                        if j == len(dataset_y) - 1:
                            for u in range(dataset_y[i][1], dataset_y[i][2] + 1):
                                res[u][dataset_y[j][0]] = "b"
                        else:
                            for u in range(dataset_y[i][1], dataset_y[i][2] + 1):
                                res[u][dataset_y[j][0]] = "a"
                    elif count == 1:
                        for u in range(dataset_y[i][1], dataset_y[i][2] + 1):
                            res[u][dataset_y[j][0]] = "b"
                    x = dataset_y[j][0]
                else:
                    target = j
                    break
            count += 1
            i = target
        if count <= 2:
            output = True
        else:
            output = False

    if output == True:
        print("YES")
        for k in res:
            print(''.join(k))
    else:
        print("NO")