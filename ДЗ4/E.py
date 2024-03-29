n = int(input())

def BinSearch(n):
    l = 1
    r = 10**18

    while l <= r:
        mid = (l + r) // 2
        S = ((1 + mid) * mid) // 2

        if S - mid < n <= S:
            return mid,S
        elif n > S:
            l = mid + 1
        elif n <= S - mid:
            r = mid - 1

def Numbering_fractions(n):
    diag, target = BinSearch(n)
    target = target - diag + 1

    if diag % 2 == 0:
        i = diag
        j = 1
        target = n - target
        return i-target,j+target
    else:
        i = 1
        j = diag
        target = n - target
        return i+target,j-target

numerator, denominato = Numbering_fractions(n)

print(f"{numerator}/{denominato}")
