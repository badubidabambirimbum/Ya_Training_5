with open("input.txt", "r") as f:
    n, m = list(map(int, f.readline().split()))
    matrix = [line.strip() for line in f]

def precalculation(matrix,n,m):
    matrix_left = [[0] * m for i in range(n)]
    matrix_right = [[0] * m for i in range(n)]

    for i in range(n):
        last = 0
        for j in range(m):
            if matrix[i][j] == "#":
                matrix_left[i][j] = last + 1
                last += 1
            else:
                last = 0

    for i in range(n-1,-1,-1):
        last = 0
        for j in range(m-1,-1,-1):
            if matrix[i][j] == "#":
                matrix_right[i][j] = last + 1
                last += 1
            else:
                last = 0

    return matrix_left, matrix_right

def Search_Plus(matrix,n,m):
    matrix_left, matrix_right = precalculation(matrix,n,m)

    l = 1
    r = min(n,m) // 3
    res = 0

    while l <= r:
        mid = (l + r) // 2
        flag = False

        for j in range(mid,m-mid):
            if flag == True:
                break
            count = 0
            for i in range(n):
                if count < mid:
                    if matrix_left[i][j] >= mid:
                        count += 1
                    else:
                        count = 0
                elif mid <= count < mid*2:
                    if matrix_left[i][j] >= mid * 2 and matrix_right[i][j] > mid:
                        count += 1
                    elif matrix_left[i][j] >= mid:
                        count = mid
                    else:
                        count = 0
                elif count >= mid*2:
                    if matrix_left[i][j] >= mid:
                        count += 1
                    else:
                        count = 0

                if count == mid * 3:
                    flag = True
                    break

        if flag == True:
            res = max(res,mid)
            l = mid + 1
        else:
            r = mid - 1

    return res

print(Search_Plus(matrix,n,m))