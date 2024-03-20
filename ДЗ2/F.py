with open("input.txt", "r") as input:
    n = int(input.readline())
    nums = list(map(int, input.readline().split()))
    a,b,k = list(map(int, input.readline().split()))

nr = nums[::-1]
nr.pop()
nr.insert(0,nums[0])

res = 0

for i in range(len(nums)):
    if nums[i] > res:
        l = i * k + 1
        r = i * k + k
        for y in range(b):
            if r >= a and l <= a: # l a r b
                res = nums[i]
                break
            elif a <= l and r <= b: # a l r b
                res = nums[i]
                break
            elif a >= l and b <= r and l <= b: # l a b r
                res = nums[i]
                break
            elif a <= l and b <= r and b >= l: # a l b r
                res = nums[i]
                break
            elif l > b:
                break
            l += len(nums) * k
            r += len(nums) * k

for i in range(len(nr)):
    if nr[i] > res:
        l = i * k + 1
        r = i * k + k
        for y in range(b):
            if r >= a and l <= a: # l a r b
                res = nr[i]
                break
            elif a <= l and r <= b: # a l r b
                res = nr[i]
                break
            elif a >= l and b <= r and l <= b: # l a b r
                res = nr[i]
                break
            elif a <= l and b <= r and b >= l: # a l b r
                res = nr[i]
                break
            elif l > b:
                break
            l += len(nums) * k
            r += len(nums) * k

print(res)