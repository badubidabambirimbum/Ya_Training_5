st = set()

with open("input.txt", "r") as input:
    n = int(input.readline())
    for i in range(n):
        x, y = tuple(map(int, input.readline().split()))
        st.add((x, y))

def square(st):
    res = []
    if len(st) == 1:
        for num in st:
            x1, y1 = num
        res = [[x1, y1 + 1], [x1 + 1, y1], [x1 + 1, y1 + 1]]
        return res
    for point1 in st:
        for point2 in st:
            if point1 != point2:
                delta_x = point1[0] - point2[0]
                delta_y = point1[1] - point2[1]

                p1 = (point1[0] + delta_y, point1[1] - delta_x)
                p2 = (point2[0] + delta_y, point2[1] - delta_x)

                p3 = (point1[0] - delta_y, point1[1] + delta_x)
                p4 = (point2[0] - delta_y, point2[1] + delta_x)

                if p1 in st and p2 in st:
                    return []
                elif p1 in st:
                    res = [p2]
                elif p2 in st:
                    res = [p1]
                if p3 in st and p4 in st:
                    return []
                elif p3 in st:
                    res = [p4]
                elif p4 in st:
                    res = [p3]

                # Диагональ
                if (point1[0] + point2[0]) % 2 == 0 and (point1[1] + point2[1]) % 2 == 0:
                    mid_point = ((point1[0] + point2[0]) // 2, (point1[1] + point2[1]) // 2)

                    mid_x = (point1[0] - point2[0]) // 2
                    mid_y = (point1[1] - point2[1]) // 2

                    p5 = (mid_point[0] + mid_y, mid_point[1] - mid_x)
                    p6 = (mid_point[0] - mid_y, mid_point[1] + mid_x)

                    if p5 in st and p6 in st:
                        return []
                    elif p5 in st:
                        res = [p6]
                    elif p6 in st:
                        res = [p5]

                if len(res) != 1:
                    res = [p1, p2]

    return res

res = square(st)

print(len(res))
for i in range(len(res)):
    print(*res[i])