with open("input.txt", "r") as input:
    t = int(input.readline())
    for i in range(t):
        n = int(input.readline())
        nums = list(map(int, input.readline().split()))
        # print(nums)
        amount = 0
        output = []
        j = 0
        while j < len(nums):
            mn = nums[j]
            sm = 0
            while j < len(nums) and sm < mn and sm < nums[j]:
                if nums[j] < mn:
                    mn = nums[j]
                sm += 1
                j += 1
            amount += 1
            output.append(sm)
        print(amount)
        print(*output)