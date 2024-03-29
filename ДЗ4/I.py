from math import sqrt

points = []

with open("input.txt", "r") as f:
    D,N = list(map(int, f.readline().split()))

    for i in range(N):
        points.append(list(map(int, f.readline().split())))

def intersection(x1,y1,x2,y2,r1,r2):
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

def check_points(x,y,t,points=points):
    for j in range(len(points)):
        x1, y1, v1 = points[j]
        r = t * v1
        if round((x - x1) ** 2 + (y - y1) ** 2,5) < round(r ** 2,5):
            return False
    return True

def check(x,y,v,D=D): # Проверка точек на 90 градусов по кругу

    p = []

    target_x1 = D
    target_y1 = 0

    target_x2 = -D
    target_y2 = 0

    target_x3 = 0
    target_y3 = D

    target_x4 = 0
    target_y4 = 0

    t1 = sqrt((x - target_x1)**2 + (y - target_y1)**2) / v
    t2 = sqrt((x - target_x2) ** 2 + (y - target_y2) ** 2) / v
    t3 = sqrt((x - target_x3) ** 2 + (y - target_y3) ** 2) / v
    t4 = sqrt((x - target_x4) ** 2 + (y - target_y4) ** 2) / v

    if check_points(target_x1, target_y1, t1):
        p.append([target_x1, target_y1, t1])
    if check_points(target_x2, target_y2, t2):
        p.append([target_x2, target_y2, t2])
    if check_points(target_x3, target_y3, t3):
        p.append([target_x3, target_y3, t3])
    # if check_points(target_x4, target_y4, t4):
    #     p.append([target_x4, target_y4, t4])

    res = [0,0,0]

    for i in range(len(p)):
        if p[i][2] > res[2]:
            res = p[i]

    return res

def f():
    pass

def Search(D, points):
    res = [0, 0, 0]
    l = 0
    r = 1000000

    while l <= r:
        mid = (l + r) / 2
        counter = 0
        counter_inside = 0
        counter_up = 0
        rejection = 0
        all = 0
        inside = False
        print(mid)
        for i in range(len(points)):
            x1, y1, v1 = points[i]
            r1 = v1 * mid
            if round((x1) ** 2 + (y1) ** 2, 5) < round((r1 - D) ** 2,5) and r1 > D:
                inside = True
                break
            p = check(x1,y1,v1)
            if p[2] > res[2]:
                res[0] = p[0]
                res[1] = p[1]
                res[2] = p[2]

            for j in range(i+1,len(points)):
                x2, y2, v2 = points[j]
                r2 = v2 * mid
                pts = intersection(x1,y1,x2,y2,r1,r2)

                for k in range(len(pts)):
                    all += 1
                    dist = sqrt(pts[k][0]**2 + pts[k][1]**2)
                    if round(dist,5) <= D and round(pts[k][1],5) >= 0:
                        counter_inside += 1
                        counter_up += 1
                        if check_points(pts[k][0],pts[k][1],mid):
                            counter += 1
                            if mid > res[2]:
                                res = [pts[k][0],pts[k][1],mid]
                        else:
                            rejection += 1
                    elif round(pts[k][1],5) >= 0:
                        counter_up += 1
        if inside == True:
            print("1")
            r = mid - 0.000000001
        elif counter > 0:
            print("2")
            l = mid + 0.000000001
        elif counter_inside == rejection and counter_inside != 0:
            print("3")
            r = mid - 0.000000001
        # elif counter_inside == 0 and counter_up != all:
        #     print("4")
        #     r = mid - 0.000000001
        else:
            print("5")
            l = mid + 0.000000001

    return res

res = Search(D, points)
res[0] = round(res[0],5)
res[1] = abs(round(res[1],5))
res[2] = round(res[2],5)

print(res[2])
print(*res[:2])

# pts = intersection(233,23,-184,154,967*0.25451119867101524,907*0.25451119867101524)
# print(pts)