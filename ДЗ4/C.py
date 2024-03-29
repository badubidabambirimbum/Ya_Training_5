def PrefSum(nums):
    prefsum = [0] * (len(nums) + 1)
    for i in range(1, len(prefsum)):
        prefsum[i] = prefsum[i-1] + nums[i-1]

    return prefsum

def BinSearch(nums, prefsum, k, s):
    l = 0
    r = len(nums) - k

    while l < r:
        mid = (l + r) // 2

        if prefsum[mid+k] - prefsum[mid] == s:
            return mid + 1
        elif prefsum[mid+k] - prefsum[mid] > s:
            r = mid - 1
        else:
            l = mid + 1

    if prefsum[l+k] - prefsum[l] == s:
        return l + 1
    else:
        return -1

with open("input.txt", "r") as f:
    n,m = list(map(int, f.readline().split()))
    nums = list(map(int, f.readline().split()))
    prefsum = PrefSum(nums)
    for i in range(m):
        l,s = list(map(int, f.readline().split()))
        print(BinSearch(nums, prefsum, l, s))