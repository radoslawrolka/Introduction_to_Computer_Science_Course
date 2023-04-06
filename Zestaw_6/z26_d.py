import math


def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i < int(math.sqrt(x)) + 1:
        if x % i == 0:
            return False
        i += 2
        if x % i == 0:
            return False
        i += 4
    return True


def to_dec(x):
    w = 0
    i = 0
    while x >0:
        if x%2 == 1:
            w += 2**i
        i += 1
        x //= 10
    return w


def zad(a, b, w=-1):
    if w == -1:
        w = 1
        a -= 1
    if a == 0:
        while b > 0:
            w = w*10
            b -= 1
        if not is_prime(to_dec(w)):
            print(w)
            print(to_dec(w))
            print()
            return 1
        else: return 0
    elif b == 0:
        while a > 0:
            w = w*10 + 1
            a -= 1
        if not is_prime(to_dec(w)):
            print(w)
            print(to_dec(w))
            print()
            return 1
        else: return 0
    return zad(a-1, b, w*10+1) + zad(a, b-1, w*10)


print(zad(2, 3))
