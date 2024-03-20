matrix = []

with open("input.txt", "r") as input:
    for i in range(8):
        matrix.append(input.readline().split()[0])


def f(matrix):
    res = set()

    for i in range(8):
        for j in range(8):
            if matrix[i][j] == "R":
                res.add((i, j))

                x = i + 1
                y = j
                while x < 8:
                    if matrix[x][y] == "*":
                        res.add((x, y))
                        x += 1
                    else:
                        break
                x = i - 1
                while x > -1:
                    if matrix[x][y] == "*":
                        res.add((x, y))
                        x -= 1
                    else:
                        break

                x = i
                y = j + 1
                while y < 8:
                    if matrix[x][y] == "*":
                        res.add((x, y))
                        y += 1
                    else:
                        break
                y = j - 1
                while y > -1:
                    if matrix[x][y] == "*":
                        res.add((x, y))
                        y -= 1
                    else:
                        break

            elif matrix[i][j] == "B":
                res.add((i, j))

                x = i + 1
                y = j + 1
                while x < 8 and y < 8:
                    if matrix[x][y] == "*":
                        res.add((x, y))
                        x += 1
                        y += 1
                    else:
                        break
                x = i - 1
                y = j + 1
                while x > -1 and y < 8:
                    if matrix[x][y] == "*":
                        res.add((x, y))
                        x -= 1
                        y += 1
                    else:
                        break

                x = i + 1
                y = j - 1
                while x < 8 and y > -1:
                    if matrix[x][y] == "*":
                        res.add((x, y))
                        x += 1
                        y -= 1
                    else:
                        break
                x = i - 1
                y = j - 1
                while x > -1 and y > -1:
                    if matrix[x][y] == "*":
                        res.add((x, y))
                        x -= 1
                        y -= 1
                    else:
                        break

            if len(res) == 64:
                return 0

    return 64 - len(res)


print(f(matrix))