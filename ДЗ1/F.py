with open("input.txt", "r") as input:
    n = int(input.readline())
    nums = list(map(int, input.readline().split()))

def f(nums):
    res = ""
    flag = False

    for i in range(1,len(nums)):
        if flag == False:
            if nums[i-1] % 2 != 0 and nums[i] % 2 != 0:
                res += "x"
                flag = True
            elif nums[i-1] % 2 == 0 and nums[i] % 2 != 0 or nums[i-1] % 2 != 0 and nums[i] % 2 == 0:
                res += "+"
                flag = True
            else:
                res += "+"
        else:
            if nums[i] % 2 != 0:
                res += "x"
            else:
                res += "+"

    return res

print(f(nums))