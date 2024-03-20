res = 0
with open("input.txt", "r") as input:
    n = int(input.readline())
    for i in range(n):
        num = int(input.readline())
        m1 = num // 4
        m2 = num % 4
        if m2 > 2:
            res += m1 + 1 + (4 - m2)
        else:
            res += m1 + m2
print(res)