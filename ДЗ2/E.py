nums = []
index = []
mx = 0
target = 0

with open("input.txt", "r") as input:
    n = int(input.readline())
    for i in range(n):
        x,y = list(map(int, input.readline().split()))
        if x - y > 0:
            target += x - y
            nums.append([x-y,x,y,i+1])
        else:
            if x > mx:
                mid = i + 1
                mx = x
            index.append(i+1)

res = target

if target + mx > res:
    res = target + mx

for i in range(len(nums)):
    if target + nums[i][2] > res:
        res = target + nums[i][2]
        mid = nums[i][3]

result = []
for i in range(len(nums)):
    if nums[i][3] != mid:
        result.append(nums[i][3])

result.append(mid)

for i in range(len(index)):
    if index[i] != mid:
        result.append(index[i])

print(res)
print(*result)