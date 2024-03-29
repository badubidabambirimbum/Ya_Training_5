n = int(input())

def BinSearch(n):
    l = 0
    r = n

    while l < r:
        mid = (l + r + 1) // 2
        target = (mid * (mid + 1) * (mid + 2)) // 6 + ((1 + mid) * mid) // 2 - 1

        if target > n:
            r = mid - 1
        else:
            l = mid

    return l

print(BinSearch(n))