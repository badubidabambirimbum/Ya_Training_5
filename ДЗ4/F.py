points = []

with open("input.txt", "r") as f:
    w, h, n = list(map(int, f.readline().split()))

    for i in range(n):
        points.append(list(map(int, f.readline().split())))

points.sort()


def precalculation(points):
    left_arr = [[0] * 2 for i in range(len(points))]
    right_arr = [[0] * 2 for i in range(len(points))]

    left_arr[0][0] = points[0][1]
    left_arr[0][1] = points[0][1]
    right_arr[-1][0] = points[-1][1]
    right_arr[-1][1] = points[-1][1]

    for i in range(1, len(left_arr)):
        left_arr[i][0] = min(left_arr[i - 1][0], points[i][1])
        left_arr[i][1] = max(left_arr[i - 1][1], points[i][1])

    for i in range(len(right_arr) - 2, -1, -1):
        right_arr[i][0] = min(right_arr[i + 1][0], points[i][1])
        right_arr[i][1] = max(right_arr[i + 1][1], points[i][1])

    return left_arr, right_arr


def starting(points):
    arr = [[points[0][0], 0, 0]]
    last = points[0][0]
    for i in range(1, len(points)):
        if last != points[i][0]:
            arr[-1][2] = i - 1
            arr.append([points[i][0], i, 0])
            last = points[i][0]
    arr[-1][2] = len(points) - 1
    return arr


def Cycle_paths(w, h, points):
    l = 1
    r = min(w, h)
    res = max(w, h)
    list1, list2 = precalculation(points)
    start = starting(points)

    while l <= r:
        mid = (l + r) // 2

        flag = False
        n = 0
        k = 0

        while k < len(start):
            if start[k][0] - start[n][0] + 1 > mid:
                i = start[n][1]
                j = start[k - 1][2] + 1

                if i > 0 and j < len(points):
                    mx = max(list1[i - 1][1], list2[j][1])
                    mn = min(list1[i - 1][0], list2[j][0])
                elif i > 0:
                    mx = list1[i - 1][1]
                    mn = list1[i - 1][0]
                elif j < len(points):
                    mx = list2[j][1]
                    mn = list2[j][0]
                else:
                    flag = True
                    break

                n += 1

                if mx - mn + 1 <= mid:
                    flag = 1
                    break
            else:
                k += 1

        if flag == False:
            i = start[n][1]
            j = start[k - 1][2] + 1

            mx = -1
            mn = 10 ** 9 + 1

            if i > 0 and j < len(points):
                mx = max(list1[i - 1][1], list2[j][1])
                mn = min(list1[i - 1][0], list2[j][0])
            elif i > 0:
                mx = list1[i - 1][1]
                mn = list1[i - 1][0]
            elif j < len(points):
                mx = list2[j][1]
                mn = list2[j][0]
            else:
                flag = True

            if mx - mn + 1 <= mid:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        if flag == True:
            res = min(res, mid)
            r = mid - 1

    return res

print(Cycle_paths(w, h, points))