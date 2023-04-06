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
    n = len(tab)
    for i in range(n):  # wiersz
        ile_liczb = 0
        for j in range(n):  # komorka
            flag_komorka = 0
            while tab[i][j] > 0:
                if is_prime(tab[i][j] % 10):
                    ile_liczb += 1
                    flag_komorka = 1
                    break
                tab[i][j] //= 10
            if flag_komorka == 0:
                break
        if ile_liczb == n:
            return True
    return False


x = [
    [1, 2, 1, 4],
    [2, 2, 4, 2],
    [5, 6, 7, 8],
    [26, 7, 5, 3]
    ]
print(zad15(x))
