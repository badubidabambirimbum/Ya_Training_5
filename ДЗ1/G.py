with open("input.txt", "r") as input:
    x = int(input.readline())
    y = int(input.readline())
    p = int(input.readline())


def f(a, b):
    counter = 1
    a -= b
    while a > 0 and b > 0:
        b -= a
        a -= b
        counter += 1

    return counter


def game(x, y, p):
    res = 100000
    dop = 0
    rounds = 1

    if x >= y:
        return rounds

    y -= x

    if x > p:
        while y > 0:
            if (p - (x - y)) != 0 and x / (p - (x - y)) > 1.618:
                dop = f(x, p - (x - y))
                if rounds + dop < res:
                    res = rounds + dop
                else:
                    return res
            y -= (x - p)
            rounds += 1
    else:
        if y >= x:
            return -1
        else:
            if x / (p - (x - y)) > 1.618:
                rounds += f(x, p - (x - y))
                return rounds
            else:
                return -1

    return rounds


print(game(x, y, p))