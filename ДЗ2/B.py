with open("input.txt", "r") as input:
    n,k = list(map(int, input.readline().split()))
    nums = list(map(int, input.readline().split()))

res = 0

if k >= len(nums) - 1:
    n1 = len(nums) - 1
    n2 = len(nums)
else:
    n1 = k
    n2 = k + 1

for i in range(len(nums)-n1):
    mn = 10**9 + 1
    mx = -1
    for j in range(i, i + n2):
        if nums[j] < mn:
            if mx - mn > res:
                res = mx - mn
            mn = nums[j]
            mx = -1
        if nums[j] > mx:
            mx = nums[j]
            if mx - mn > res:
                res = mx - mn

print(res)