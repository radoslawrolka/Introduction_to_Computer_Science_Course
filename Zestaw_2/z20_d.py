def common_digit(x, y, s):
    D = [False] * s
    while x != 0:
        d = x % s
        D[d] = [True]
        x //= s
    while y != 0:
        if D[y % s]:
            return True
        y //= s
    return False


def czy_ma_wspolne(a, b):
    s = 2
    for s in range(2, 17):
        if common_digit(a, b, s) == False:
            print(s)
            break
    else:
        print("brak systemu")


czy_ma_wspolne(20, 7)
