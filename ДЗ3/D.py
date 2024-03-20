with open("input.txt", "r") as input:
    n,k = list(map(int, input.readline().split()))
    nums = list(map(int, input.readline().split()))

def repeat(nums,k):
    d = {}

    for i in range(len(nums)):
        if nums[i] in d:
            if i - d[nums[i]] <= k:
                return True
        d[nums[i]] = i

    return False

if repeat(nums,k):
    print("YES")
else:
    print("NO")