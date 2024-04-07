from math import sqrt

points = []

with open("input.txt", "r") as f:
    D,N = list(map(int, f.readline().split()))

    for i in range(N):
        points.append(list(map(int, f.readline().split())))

def intersection(x1,y1,x2,y2,r1,r2):
    '''Поиск точек пересечения окружностей'''
    x3 = x2 - x1
    y3 = y2 - y1
    A = -2 * x3
    B = -2 * y3
    C = x3**2 + y3**2 + r1**2 - r2**2

    x0 = -(A * C) / (A**2 + B**2)
    y0 = -(B * C) / (A**2 + B**2)

    if (x1-x2)**2 + (y1-y2)**2 > (r1 + r2)**2: # Первая проверка на пересечение, вторая на вхождение одной окружности в другую
        return []
    elif (x1-x2)**2 + (y1-y2)**2 < (r1 - r2)**2:
        return []
    elif (x1-x2)**2 + (y1-y2)**2 == (r1 + r2)**2:
        return [[x0+x1,y0+y1]]

    d = sqrt(r1**2 - (C**2 / (A**2 + B**2)))
    mult = sqrt(d**2 / (A**2 + B**2))

    ax = x0 + B * mult + x1
    ay = y0 - A * mult + y1
    bx = x0 - B * mult + x1
    by = y0 + A * mult + y1

    return [[ax,ay],[bx,by]]

def check_point(x, y, t, points=points):
    '''Проверка на то, что точка не входит в другие окружности'''

    for j in range(len(points)):
        x1, y1, v1 = points[j]
        r = t * v1
        if round((x - x1) ** 2 + (y - y1) ** 2,5) < round(r ** 2,5):
            return False
    return True

def check(x,y,v,D=D):
    '''Проверка точек на 90 градусов по кругу'''

    p = []

    target_x1 = D
    target_y1 = 0

    target_x2 = -D
    target_y2 = 0

    target_x3 = 0
    target_y3 = D

    t1 = sqrt((x - target_x1)**2 + (y - target_y1)**2) / v
    t2 = sqrt((x - target_x2) ** 2 + (y - target_y2) ** 2) / v
    t3 = sqrt((x - target_x3) ** 2 + (y - target_y3) ** 2) / v

    if check_point(target_x1, target_y1, t1):
        p.append([target_x1, target_y1, t1])
    if check_point(target_x2, target_y2, t2):
        p.append([target_x2, target_y2, t2])
    if check_point(target_x3, target_y3, t3):
        p.append([target_x3, target_y3, t3])

    res = [0,0,0]

    for i in range(len(p)):
        if p[i][2] > res[2]:
            res = p[i]

    return res


def create_points_on_circle(D,step=D/60):
    '''Формирование массива точек внутри окружности'''

    points = []
    x = -D
    while x < D + 1:
        y = 0
        while y < D + 1:
            if x**2 + y**2 <= D**2:
                points.append([x,y])
            y += step
        x += step

    return points

def Determining_Search_Distance(D=D, points=points):
    '''Поиск левой и правой границы'''

    l = 0
    r = 1000000

    check_circle = create_points_on_circle(D)
    true_points = []

    while l <= r:
        mid = (l + r) / 2
        counter = 0
        true_points.clear()

        for i in range(len(check_circle)):
            x, y = check_circle[i]
            if check_point(x,y,mid):
                true_points.append([x,y])
                counter += 1

        if 0 < counter <= 3:
            l = mid + 0.000000001
            return l,r,true_points
        elif counter == 0:
            r = mid - 0.000000001
        else:
            l = mid + 0.000000001

    return l,r

def Search(D, points):
    '''Поиск самой дальней точки'''

    res = [0, 0, 0]
    l,r,true_points = Determining_Search_Distance()

    new_points_set = set()
    new_points = list()

    # Выбираем окружности, которые пересекаются с окрестностью точек из Determining_Search_Distance()
    for i in range(len(points)):
        for j in range(len(true_points)):
            if round((points[i][0] - true_points[j][0]) ** 2 + (points[i][1] - true_points[j][1]) ** 2,5) < round((l * points[i][2] + D / 15) ** 2,5) and tuple(points[i]) not in new_points_set:
                new_points_set.add(tuple(points[i]))
                new_points.append(points[i])

    while l <= r:
        mid = (l + r) / 2
        counter = 0

        for i in range(len(new_points)):
            x1, y1, v1 = new_points[i]
            r1 = v1 * mid

            p = check(x1,y1,v1)
            if p[2] > res[2]:
                res[0] = p[0]
                res[1] = p[1]
                res[2] = p[2]

            for j in range(i+1,len(new_points)):
                x2, y2, v2 = new_points[j]
                r2 = v2 * mid
                if x1 == x2 and y1 == y2:
                    continue
                else:
                    pts = intersection(x1,y1,x2,y2,r1,r2)

                    for k in range(len(pts)):
                        dist = sqrt(pts[k][0]**2 + pts[k][1]**2)
                        if round(dist,5) <= D and round(pts[k][1],5) >= 0:
                            if check_point(pts[k][0], pts[k][1], mid):
                                counter += 1
                                if mid > res[2]:
                                    res = [pts[k][0],pts[k][1],mid]

        if counter > 0:
            l = mid + 0.000000001
        else:
            r = mid - 0.000000001

    return res

res = Search(D, points)
res[0] = round(res[0],5)
res[1] = abs(round(res[1],5))
res[2] = round(res[2],5)

print(res[2])
print(*res[:2])