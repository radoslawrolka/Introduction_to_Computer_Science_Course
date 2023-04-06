import math


def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i < math.sqrt(x) + 1:
        if x % i == 0:
            return False
        i += 2
        if x % i == 0:
            return False
        i += 4
    return True


def zad15(tab):
    czy_pierwsza = 0
    prev = 1
    curr = 1
    for i in range(len(tab)):
        if i == curr:
            prev, curr = curr, prev + curr
            if is_prime(tab[i]):
                return False
        else:
            if not czy_pierwsza:
                if is_prime(tab[i]):
                    czy_pierwsza = 1
    if czy_pierwsza == 1:
        return True
    else:
        return False


print(zad15([0, 4,6, 8,6,12,13,16,11,6]))
