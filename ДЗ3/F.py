with open("input.txt", "r") as input:
    st = set(input.readline().split())
    words = input.readline().split()

res = []

for w in words:
    target = ""
    for i in range(len(w)):
        target += w[i]
        if target in st:
            break
    res.append(target)

print(*res)