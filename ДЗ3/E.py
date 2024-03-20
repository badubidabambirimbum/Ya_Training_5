with open("input.txt", "r") as input:
    n = int(input.readline())
    s1 = set(map(int, input.readline().split()))
    n = int(input.readline())
    s2 = set(map(int, input.readline().split()))
    n = int(input.readline())
    s3 = set(map(int, input.readline().split()))

res = sorted(list(s1 & s2 | s1 & s3 | s2 & s3))

print(*res)