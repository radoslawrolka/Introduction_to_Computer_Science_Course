def ilecyfr(x):
    i = 0
    while x > 0:
        x = x//10
        i += 1
    return i


def czycyfra(x, y):
    while x > 0:
        if x%10 == y:
            return True
        x = x//10
    return False


def czy_ma_cyfre(x):
    ile = ilecyfr(x)
    print(czycyfra(x, ile))


czy_ma_cyfre(123463)
