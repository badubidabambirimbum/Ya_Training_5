matrix = []
nums = []

with open("input.txt", "r") as input:
    n,m = list(map(int, input.readline().split()))
    for i in range(n):
        matrix = list(map(int, input.readline().split()))
        for j in range(m):
            nums.append([matrix[j],i,j])

mx = -1
for i in range(len(nums)):
    if nums[i][0] > mx:
        mx = nums[i][0]
        target1 = nums[i][1]
        target3 = nums[i][2]

check1 = [False] * len(nums)
check2 = [False] * len(nums)

for i in range(len(nums)):
    if nums[i][1] == target1:
        check1[i] = True
    if nums[i][2] == target3:
        check2[i] = True

mx1 = -1
mx2 = -1
for i in range(len(nums)):
    if nums[i][0] > mx1 and check1[i] == False:
        mx1 = nums[i][0]
        target2 = nums[i][2]
    if nums[i][0] > mx2 and check2[i] == False:
        mx2 = nums[i][0]
        target4 = nums[i][1]

for i in range(len(nums)):
    if nums[i][2] == target2:
        check1[i] = True
    if nums[i][1] == target4:
        check2[i] = True

res1 = -1
res2 = -1
for i in range(len(check1)):
    if check1[i] == False and nums[i][0] > res1:
        res1 = nums[i][0]
    if check2[i] == False and nums[i][0] > res2:
        res2 = nums[i][0]

if res1 > res2:
    print(target4+1,target3+1)
else:
    print(target1+1,target2+1)