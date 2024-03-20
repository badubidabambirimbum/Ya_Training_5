with open("input.txt", "r") as input:
    n,k,d = list(map(int, input.readline().split()))

def f(n,k,d):
    x = str(n)
    target = int(x + "9")
    if target % k < 10:
        x += str(9 - target%k)
    else:
        return -1
    x += "0" * (d-1)
    return x

print(f(n,k,d))