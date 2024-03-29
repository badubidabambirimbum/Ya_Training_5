parties = []
sm = 0

with open("input.txt", "r") as f:
    n = int(f.readline())

    for i in range(1,n+1):
        v,p = list(map(int, f.readline().split()))
        sm += v
        parties.append([v,p,i])

parties.sort()
# print(parties)

def PrefSum(nums):
    prefsum = [0] * (len(nums) + 1)
    for i in range(1, len(prefsum)):
        prefsum[i] = prefsum[i-1] + nums[i-1][0]
    return prefsum

def BinS(parties, people):
    l = 0
    r = len(parties) - 1

    while l < r:
        mid = (l + r) // 2

        if parties[mid][0] >= people:
            r = mid
        else:
            l = mid + 1

    if parties[l][0] >= people:
        return l
    else:
        return -1

def Search(prefsum, parties,x,i,sm=sm):
    l = 1
    r = sm
    res = 10**6 + 1

    while l <= r:
        mid = (l + r) // 2 # сколько будет у нас

        index = BinS(parties, mid)

        if index > -1:
            target = (prefsum[-1] - prefsum[index]) - (mid-1) * (len(parties) - index) + x[0]
            if i >= index:
                target -= x[0] - (mid-1)
            if target > mid:
                if res > target:
                    res = target # кол-во людей у меня
                l = mid + 1
            else:
                if res > mid:
                    res = mid # кол-во людей у меня
                r = mid - 1
        else:
            if mid <= sm and res > mid:
                res = mid
            r = mid - 1

    return res

res = [0,0,10**15,0]
summa = 0
prefsum = PrefSum(parties)

for i in range(len(parties)):
    if parties[i][1] != -1:
        target = Search(prefsum, parties,parties[i],i)

        if res[2] > target - parties[i][0] + parties[i][1]:
            res[2] = target - parties[i][0] + parties[i][1] # затраты
            res[3] = parties[i][2] # индекс
            res[0] = target # кол-во людей у меня
            summa = res[0] - parties[i][0]

res_array = [0] * len(parties)

for i in range(len(parties)):
    if parties[i][2] == res[3]:
        res_array[parties[i][2]-1] = res[0]
    elif parties[i][0] >= res[0]:
        summa -= (parties[i][0] - (res[0] - 1))
        res_array[parties[i][2]-1] = res[0] - 1
    else:
        res_array[parties[i][2]-1] = parties[i][0]

if summa != 0:
    for i in range(len(parties)-1,-1,-1):
        if i != res[3] - 1:
            if res_array[i] >= summa:
                res_array[i] -= summa
                summa = 0
            else:
                summa -= (res_array[i] - 1)
                res_array[i] = 1

print(res[2])
print(res[3])
print(*res_array)
