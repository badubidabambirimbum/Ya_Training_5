def L_BinSearch(nums, L):
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < L:
            l = mid + 1
        else:
            r = mid
    return l

def R_BinSearch(nums, R):
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l + r + 1) // 2
        if nums[mid] > R:
            r = mid - 1
        else:
            l = mid
    return l

result = []

with open("input.txt", "r") as f:
    n = int(f.readline())
    nums = list(map(int, f.readline().split()))
    nums.sort()
    k = int(f.readline())
    for i in range(k):
        L, R = list(map(int, f.readline().split()))
        l = L_BinSearch(nums,L)
        r = R_BinSearch(nums,R)
        if nums[l] >= L and nums[r] <= R:
            result.append(r - l + 1)
        else:
            result.append(0)

print(*result)
