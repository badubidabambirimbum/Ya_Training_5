from collections import defaultdict
dict = defaultdict(int)

with open("input.txt", "r") as input:
    n = int(input.readline())

    for i in range(n):
        m = int(input.readline())
        songs = input.readline().split()
        for song in songs:
            dict[song] += 1

result = []

for key in dict:
    if dict[key] == n:
        result.append(key)

result.sort()

print(len(result))
print(*result)