from collections import Counter

with open("input.txt", "r") as input:
    n = int(input.readline())
    nums = Counter(map(int, input.readline().split()))

mx = 0

for key in nums:
    if nums[key] > mx:
        mx = nums[key]
    if key + 1 in nums and nums[key+1] + nums[key] > mx:
        mx = nums[key+1] + nums[key]
    if key - 1 in nums and nums[key-1] + nums[key] > mx:
        mx = nums[key-1] + nums[key]

print(n-mx)