with open("input.txt", "r") as input:
    n = int(input.readline())
    nums = list(map(int, input.readline().split()))

s = sum(nums)
mx = max(nums)

if s - mx < mx:
    print(mx - (s - mx))
else:
    print(s)