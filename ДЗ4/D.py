with open("input.txt", "r") as f:
    w,n,m = list(map(int, f.readline().split()))
    list1 = list(map(int, f.readline().split()))
    list2 = list(map(int, f.readline().split()))

def check(nums, w):
    i = 0
    j = 1
    n = 0
    while n < len(nums):
        if nums[n] > w:
            return -1
        if i + nums[n] <= w:
            i += nums[n] + 1
        elif i + nums[n] > w:
            i = nums[n] + 1
            j += 1
        n += 1
    if i == 0:
        return j - 1
    return j

def BinSearch(w,list1,list2):
    l = 0
    r = w
    res = 1000000

    while l <= r:
        mid = (l + r) // 2

        num1 = check(list1,mid)
        num2 = check(list2,w-mid)

        if num1 == -1:
            l = mid + 1
        elif num2 == -1:
            r = mid - 1
        elif num1 > num2:
            l = mid + 1
            res = min(res, num1)
        elif num1 < num2:
            r = mid - 1
            res = min(res, num2)
        elif num1 == num2:
            return num1

    return res

print(BinSearch(w,list1,list2))